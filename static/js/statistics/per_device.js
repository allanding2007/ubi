var jsonDataCall;
var id = device_id;
$(function() {
    $.get("/statistic/per/device/ajax/" + id.toString(), function(result){
        jsonDataCall = result;
        $('#id_table').bootstrapTable({
            data: jsonDataCall.data,
            pagination: true,
            pageSize: 5,
            pageList: [5, 10],
            onClickRow: function(row, $element){
                console.log(row);
                //id = row.device_id
                //window.location = "/statistics/device_detail/" + id;
            }
        });
    });
});



