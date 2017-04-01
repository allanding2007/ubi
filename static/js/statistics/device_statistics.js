
var jsonDataCall ;

$(function() {
    $.get("/statistics/devices/ajax/", function(result){
        jsonDataCall = result;
        $('#id_table').bootstrapTable({
            data: jsonDataCall.data,
            pagination: true,
            pageSize: 5,
            pageList: [5, 10],
            onClickRow: function(row, $element){
                console.log(row);
                id = row.device_id
                window.location = "/statistics/device_detail/" + id;
            }
        });
    });
});



