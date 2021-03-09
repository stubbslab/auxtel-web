$(document).ready(function(){
      refreshTable();
    });

    function refreshTable(){
        $('#tableHolder').load(window.location.href + " #tableHolder" , function(){
           setTimeout(refreshTable, 10000);
        });
    }
