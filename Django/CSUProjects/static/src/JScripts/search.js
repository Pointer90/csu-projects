const cards = document.querySelectorAll(".card-search-element");
const searchForm = document.getElementById('search');
const searchField = document.getElementById('search-field')

searchForm.addEventListener('submit', function(event) {
    event.preventDefault();

    const query = searchField.value.toLowerCase();

    // Отправляем запрос на сервер
    fetch(`/search?search=${query}`)
        .then(response => response.json())
        .then(data => {updateCardsVisibility(JSON.parse(data));})
        .catch(error => console.error('Ошибка при выполнении запроса:', error));
});

// Функция для обновления видимости карточек на странице
function updateCardsVisibility(data) {
    // pids - project indexes
    const pids = data.map(item => item.pk);
    var nf = document.getElementById('not-found').classList;

    cards.forEach(card => {
        let cardId = parseInt(card.id);
        let cardWrap = card.classList

        if (pids.includes(cardId))
            cardWrap.remove('visually-hidden')
        else
            cardWrap.add('visually-hidden')
    });

    if (pids.length > 0){
        nf.add('visually-hidden');
    }
    else{
        nf.remove('visually-hidden');
    }
}
