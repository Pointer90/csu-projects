const elements = document.querySelectorAll(".card-title");
const searchForm = document.forms[0];

searchForm.addEventListener('submit', function(event) {
    event.preventDefault();

    const query = searchForm[0].value.toLowerCase();

    // Отправляем запрос на сервер
    fetch(`/search?search=${query}`)
        .then(response => response.json())
        .then(data => {
            // Обрабатываем полученные данные
            updateCardsVisibility(JSON.parse(data));
        })
        .catch(error => console.error('Ошибка при выполнении запроса:', error));
});

// Функция для обновления видимости карточек на странице
function updateCardsVisibility(data) {
    const pids = data.map(item => item.pk);
    var nf = document.querySelector('#nf');

    elements.forEach(element => {
        if (pids.includes(parseInt(element.id)))
            element.closest('.card').classList.remove('visually-hidden')
        else
            element.closest('.card').classList.add('visually-hidden')
    });

    //TODO: Переименуй 
    if (pids.length > 0){
        nf.classList.add('visually-hidden');       
    }
    else{
        nf.classList.remove('visually-hidden');
    }
}
