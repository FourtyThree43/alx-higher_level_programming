$(document).ready(() => {
  function translateHello () {
    const languageCode = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/?lang=${languageCode}`, (data) => {
      $('#hello').html(data.hello);
    });
  }

  $('#btn_translate').click(translateHello);

  $('#language_code').keypress((e) => {
    if (e.which === 13) {
      translateHello();
    }
  });
});
