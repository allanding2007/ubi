
var jsonDataCall ;

$(function() {
    $.get("/ssids/ajax/", function(result){
        jsonDataCall = result;
        $('#id_table').bootstrapTable({
            data: jsonDataCall,
            pagination: true,
            pageSize: 5,
            pageList: [5, 10],
            onClickRow: function(row, $element){
                console.log(row);
                id = row.id
                window.location = "/ssids/ssid/edit/" + id;
            }
        });
    });
});