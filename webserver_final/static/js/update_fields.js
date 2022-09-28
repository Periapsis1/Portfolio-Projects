
var table_head_items = [];
var row_options = [];
var table_data = [];
var table_row_elements = [];

function populate_input_fields(row) {
    let idx = row.target.selectedIndex;
    let form = document.getElementsByClassName('db-update-form')[0];
    let target_row_data = table_data[idx];
    for (const key in target_row_data) {
        let element = form.getElementsByClassName(key)[0];
        if (element !== undefined){
            // check if element is a date element, and convert it to yyy-MM-dd format
            if (element.type === 'date') {
                let date = new Date(target_row_data[key]);
                element.value = date.toISOString().substring(0, 10);
            } else {
                element.value = target_row_data[key];
            }
        }
    }
}

function main () {
    let table_head_elements = document.getElementsByClassName('db-table-head-item');

    for (let i = 0; i < table_head_elements.length; i++)
        table_head_items.push(table_head_elements[i].innerText);

    let row_element = document.getElementsByClassName('update-row-select')[0];

    let row_option_elements = row_element.options;
    for (let i = 0; i < row_option_elements.length; i++)
        row_options.push(row_option_elements[i].value);


    table_row_elements = document.getElementsByClassName('db-table-body-row');

    populate_input_fields({target: row_element});
    row_element.addEventListener('change', populate_input_fields);
}

// only activate if the table supports update operations
if (crud_operations.includes('U')) {
    fetch('/tables/' + table_name + '/get_data', {
        method: 'GET'
    }).then(res => res.json())
    .then(data => {
        table_data = data;
        main();
    });
}