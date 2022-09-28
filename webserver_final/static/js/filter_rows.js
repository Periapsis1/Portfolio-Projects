
function filter_table_old() {  // This seems easier as a search function, but this is a Database course not a web development course
    let table_rows = document.getElementsByClassName('db-table-body-row');
    for (let i = 0; i < table_rows.length; i++) {
        let row_data = table_rows[i].getElementsByClassName('db-table-body-item');
        let row_text = '';
        for (let j = 0; j < row_data.length; j++)
            row_text += row_data[j].innerText.toLowerCase();
        if (row_text.includes(query))
            table_rows[i].style.display = '';
        else
            table_rows[i].style.display = 'none';
    }
}

function filter_table() {
    let input_element = document.getElementById('search-input');
    let query = input_element.value;
    // Convert the table name from camel case to snake case
    let table_name_ = table_name.replace(/([a-z])([A-Z])/g, '$1_$2').toLowerCase();
    // redirect to the current table page with query as the argument. if query is empty, redirect to the current table page without an argument
    if (query === '- None -') {
        window.location.href = '/tables/' + table_name_;
    } else {
        window.location.href = '/tables/' + table_name_ + '?search=' + query;
    }
}