document.addEventListener('DOMContentLoaded', function() {
    // Функція для завантаження та відображення списку завдань
    function loadModels() {
        fetch('/api/technique')
            .then(response => response.json())
            .then(models => {
                const modelsList = document.getElementById('models-list');
                console.log(modelsList)
                // Очищаємо список перед додаванням нових даних
                modelsList.innerHTML = '';
                models.forEach(model => {
                    const row = modelsList.insertRow();
                    row.innerHTML = `
                        <td>${model.id}</td>
                        <td>${model.name}</td>
                        <td>${model.desc}</td>
                        <td>${model.status}</td>
                        <td>${model.date_time}</td>
                    `;
                });
            });
    }

    // Викликаємо функцію для ініціалізації списку записів
    loadModels();

    // функція додавання даних на сервер
    function addModel(data) {
        fetch('/api/technique', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(() => {
            // Очищаємо форму після додавання запису
            document.getElementById('model-form').reset();
            // Видаляємо значення ID для уникнення непередбачуваної поведінки
            document.getElementById('id').value = '';
            // Оновлюємо список записів на сторінці
            loadModels();
        })
        .catch(error => console.error('Error:', error));
    }

    // функція видаленняs
    function deleteModel(id) {
        let path = '/api/technique/' + id
        fetch(path, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            loadModels();
        })
        .catch(error => console.error('Error:', error));
    }

    // EventHandler для форми додавання нового запису
    document.getElementById('model-form').addEventListener('submit', function(event) {
        event.preventDefault();

        const id = document.getElementById('id').value;  // Отримуємо ID
        const name = document.getElementById('name').value;
        const desc = document.getElementById('desc').value;
        const status = document.getElementById('status').value;
        const date_time = document.getElementById('date_time').value;

        const data = {
            id: id,
            name: name,
            desc: desc,
            status: status,
            date_time: date_time
        };

        // Відправляємо дані на сервер для додавання або оновлення запис
        addModel(data);
    });

    document.getElementById('model-form-delete').addEventListener('submit', function(event) {
        event.preventDefault();

        model_id = document.getElementById('model_id').value;

        model_id = (model_id < 1) ? (model_id * -1) : model_id // на випадок відʼємних значень

        // Видалення по id
        deleteModel(model_id);
    });
});