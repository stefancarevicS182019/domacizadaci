$(document).ready(function () {
    $("#unos2").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#tabela tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
    $(".predavaci").click(function () {
        var value = $(this).html().toLowerCase();
        $("#unos2").val(value);
        $("#tabela tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
    $(".ucionice").click(function () {
        var value = $(this).html().toLowerCase();
        $("#unos2").val(value);
        $("#tabela tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});