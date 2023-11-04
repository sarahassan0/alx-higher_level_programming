$(document).ready(function () {
    $('#btn_translate').click(fetchTranslation);
    $('#language_code').keypress(function (e) {
        if (e.keyCode == 13) {
            fetchTranslation();
        }
    });

    function fetchTranslation() {
        var languageCode = $('#language_code').val();

        $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode, function (data) {
            $('#hello').text(data.hello);
        });
    }
});
