# https://docs.peewee-orm.com/en/latest/peewee/querying.html#deleting-records

from flask import Blueprint, jsonify, request
from Models.technique_model import Model

technique_api = Blueprint('technique_api', __name__)


@technique_api.route('/technique', methods=['GET'])
def get_models():
    models = [m for m in Model.select()]
    return jsonify([
        {'id': m.id, 'name': m.name, 'desc': m.desc,
         'status': m.status, 'date_time': m.date_time}
        for m in models
    ])


@technique_api.route('/technique', methods=['POST'])
def add_or_update_model():
    data = request.get_json()
    print(data)

    #  Перевіряємо чи переданий ID, це ключове поле яке не може бути пустим
    model_id = int(data.get('id')) if 'id' in data and data['id'] else None

    if model_id:
        # Спроба знайти існуючий запис
        model = Model.get_or_none(Model.id == model_id)
        if model:
            # Оновлення існуючих записів
            model.name = data['name']
            model.desc = data['desc']
            model.status = data['status']
            model.date_time = data['date_time']
            model.save()
        else:
            # Якщо запису не знайдено, створюємо новий з вказаним ID
            model = Model.create(id=model_id, **data)
    else:
        # Видалення 'id' з даних, щоб уникнути конфліктів з NULL значеннями
        data.pop('id', None)
        # Створення нового запису без вказання ID
        model = Model.create(**data)

    return jsonify({
        'id': model.id, 'name': model.name, 'desc': model.desc,
        'status': model.status, 'date_time': model.date_time
    }), 200 if model_id else 201


@technique_api.route('/technique/<int:model_id>', methods=['DELETE'])
def delete_model(model_id):
    print(model_id)
    try:
        model = Model.get(model_id)
        print(model)
        model.delete_instance()
        return jsonify({'message': 'Record deleted successfully'}), 200
    except Model.DoesNotExist:
        return jsonify({'message': 'Record does not exist'}), 404
    except Exception as e:
        return jsonify({'message': e}), 500

