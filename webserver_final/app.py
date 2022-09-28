from flask import Flask, render_template, jsonify, abort, request, redirect, url_for
from flask_mysqldb import MySQL
from config_sql import configure_app
from jinja2 import Template
import os

import table_manipulation as tm
import util.util as util

# Configuration

app = Flask(__name__)

configure_app(app)

mysql = MySQL(app)

tm.mysql = mysql

def sql_query(query):
    with mysql.connection.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

def sql_query_with_input(query, args):
    with mysql.connection.cursor() as cur:
        cur.execute(query, args)
        cur.connection.commit()
        return cur.fetchall()

def query_table_to_list(table, column):
    query = f"SELECT {column} FROM {table};".replace('$.', f'{table}.')
    result = sql_query(query)
    return [list(row.values())[0] for row in result]

@app.get('/')
def root():
    return render_template(
        "site_list.jinja",
        subpage_name='home',
        tables=tm.tables,
        sites=tm.tables,
        camel_to_snake=util.camel_to_snake
    )

@app.get('/tables/<table>')
def site_list(table):
    search_filter = request.args.get('search', default=None, type=str)
    table = util.snake_to_camel(table)
    if table not in tm.tables:
        abort(404)
    if table == 'VisitDiagnoses':
        if search_filter:
            query = tm.sql_filter_queries[table]
            arg = (search_filter,)
            table_data = sql_query_with_input(query, arg)
        else:
            table_data = sql_query(tm.sql_get_queries[table])

        diagnosis_list = ['-- select a diagnosis --', '- None -'] + query_table_to_list('Diagnoses', 'Diagnoses.name')
    else:
        table_data = sql_query(tm.sql_get_queries[table])
        diagnosis_list = []

    table_columns = list(sql_query(tm.sql_get_queries[table])[0].keys())

    update_options = [
        ' '.join(str(row[option]) for option in tm.row_drop_down_select[table])
        for row in table_data
    ]
    
    return render_template(
        'table.jinja',
        subpage_name=table,
        tables=tm.tables,
        snake_name=util.camel_to_snake(table),
        table_columns=table_columns,
        table_info=tm.table_crud_operations[table],
        table_data=table_data,
        input_fields=tm.get_sql_input_fields(table),
        update_options=update_options,
        diagnosis_list=diagnosis_list,
        camel_to_snake=util.camel_to_snake,
        zip=zip,
        list=list
    )

@app.get('/tables/<table>/get_data')
def get_row_data(table):
    if table in tm.tables:
        table_data = sql_query(tm.sql_get_queries[table])
        return jsonify(table_data)
    else:
        abort(404)

@app.post('/tables/<table>/add_row')
def add_row(table):
    table = util.snake_to_camel(table)
    form = request.form
    if table in tm.tables:
        query = tm.sql_create_queries[table]
        args = []
        for field_info in tm.get_sql_input_fields(table):
            if field_info['type'] == 'checkbox':
                field = 1 if field_info['name'] in form else 0
            else:
                field = form[field_info['name']]
            args.append(field)

        sql_query_with_input(query, args)
    else:
        abort(404)
    '''
    if table == 'Visits':
        query = """
        INSERT INTO Visits (`date`, `reason_for_visit`, `patient_id`, `provider_id`, `nurse_id`)
        VALUES (
            %s,
            %s,
            (SELECT patient_id
                FROM Patients
                WHERE CONCAT(first_name, ' ', last_name) = %s),
            (SELECT provider_id
                FROM Providers
                WHERE CONCAT(first_name, ' ', last_name) = %s),
            (SELECT nurse_id
                FROM Nurses
                WHERE CONCAT(first_name, ' ', last_name) = %s));"""
        sql_query_with_input(query, (
            form['date_input'],
            form['reason_for_visit_input'],
            form['patient_name_input'],
            form['provider_name_input'],
            form['nurse_name_input']
        ))
    '''
    return redirect('/tables/' + util.camel_to_snake(table))

@app.post('/tables/<table>/update_row')
def edit_row(table):
    table = util.snake_to_camel(table)
    form = request.form
    if table == 'Visits':
        query = """
        UPDATE Visits
        SET `date` = %s,
            `reason_for_visit` = %s,
            `patient_id` = (SELECT patient_id
                FROM Patients
                WHERE CONCAT(first_name, ' ', last_name) = %s),
            `provider_id` = (SELECT provider_id
                FROM Providers
                WHERE CONCAT(first_name, ' ', last_name) = %s),
            `nurse_id` = (SELECT nurse_id
                FROM Nurses
                WHERE CONCAT(first_name, ' ', last_name) = %s)
        WHERE `visit_id` = %s;"""
        sql_query_with_input(query, (
            form['date_input'],
            form['reason_for_visit_input'],
            form['patient_name_input'],
            form['provider_name_input'],
            form['nurse_name_input'],
            form['row-select'].split(' ')[0]
        ))
    else:
        abort(404)
    return redirect('/tables/' + util.camel_to_snake(table))

@app.post('/tables/<table>/delete_row')
def delete_row(table):
    table = util.snake_to_camel(table)
    form = request.form
    if table == 'Visits':
        query = """
        DELETE FROM Visits
        WHERE `visit_id` = %s;"""
        sql_query_with_input(query, (
            form['row-select'].split(' ')[0],),
        )
    return redirect('/tables/' + util.camel_to_snake(table))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 21118))
    
    app.run(port=port)