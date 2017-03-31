
var jsonDataCall ;

$(function() {
    $.get("http://0.0.0.0:5000/assets/devices/ajax/", function(result){
        jsonDataCall = result;
        $('#id_table').bootstrapTable({
            data: jsonDataCall,
            pagination: true,
            pageSize: 5,
            pageList: [5, 10],
            onClickRow: function(row, $element){
                console.log(row);
                id = row.id
                window.location = "/assets/device/edit/" + id;
            }
        });
    });
});