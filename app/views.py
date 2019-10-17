from flask import current_app, redirect, render_template, url_for
from sqlalchemy.exc import SQLAlchemyError

from app import view
from .forms import DrinkForm, StoreForm
from .models import *


@view.route('/')
def home():
    return render_template('home.html')


@view.route('/stores', methods=['GET'])
def dashboard_stores():
    stores = Store.query.all()
    return render_template('dashboard-stores.html', stores=stores)


@view.route('/store', methods=['POST'])
def create_store():
    form = StoreForm()

    if form.validate_on_submit():
        store = Store(form.name.data, form.comments.data)
        try:
            db.session.add(store)
            db.session.commit()
        except SQLAlchemyError:
            current_app.logger.info("error adding new store")
        current_app.logger.info("added new store")
        return redirect(url_for('view.dashboard_stores'))

    return render_template('store-form.html', form=form)


@view.route('/store/<int:store_id>',  methods=['POST', 'DELETE'])
def delete_store(store_id):
    try:
        Store.query.filter_by(id=store_id).delete()
        db.session.commit()
    except SQLAlchemyError:
        current_app.logger.info("error deleting store with id {}".format(store_id))
    current_app.logger.info("deleted store with id {}".format(store_id))
    return redirect(url_for('view.dashboard_stores'))


@view.route('/store/<string:store>', methods=['GET'])
def dashboard_drinks(store):
    drink = Drink.query.filter_by(store=store).all()
    return render_template('dashboard-drinks.html', drinks=drink, store=store)


@view.route('/store/<string:store>/drink', methods=['POST'])
def create_drink(store):
    form = DrinkForm()
    if form.validate_on_submit():
        drink = Drink(store=store,
                      name=form.name.data,
                      sugar_level=form.sugar_level.data,
                      ice_level=form.ice_level.data,
                      rating=form.rating.data,
                      comments=form.comments.data)
        try:
            db.session.add(drink)
            db.session.commit()
        except SQLAlchemyError:
            current_app.logger.info("error adding new drink to store {}".format(store))
        current_app.logger.info("added new drink to store {}".format(store))
        return redirect(url_for('view.dashboard_drinks', store=store))
    return render_template('drink-form.html', form=form, store=store)


@view.route('/store/<string:store>/drink/<int:drink_id>',  methods=['POST', 'DELETE'])
def delete_drink(store, drink_id):
    try:
        Drink.query.filter_by(id=drink_id).delete()
        db.session.commit()
    except SQLAlchemyError:
        current_app.logger.info("error deleting drink with id {}".format(drink_id))
    current_app.logger.info("deleted drink with id {}".format(drink_id))
    return redirect(url_for('view.dashboard_drinks', store=store))
