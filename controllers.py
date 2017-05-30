from sys import exit
from configparser import RawConfigParser


from phonebook import PhoneBook
import views
from serialize import Serialize


def enter_subscribers_data(key):
    if key == 'subscriber':
        value = views.enter_subscriber()
    else:
        value = views.enter_phone_number()
    return value


class Controller:

    def __init__(self):
        config = RawConfigParser()
        config.read('serialize_conf.cfg')
        serializer = Serialize(config.get('Serialize', 'serialize'))
        PhoneBook.get_object().set_serializer(serializer)
        PhoneBook.get_object().load_database()

    @staticmethod
    def add_new_subscriber():
        sub, num = views.enter_new_subscriber_and_phone_number()
        found = PhoneBook.get_object().find_subscriber('subscriber', sub)
        if found is not None:
            found = PhoneBook.get_object().find_subscriber('phone', num)
            if found is not None:
                views.print_result_of_adding(-1)
                return
        views.print_result_of_adding(
            PhoneBook.get_object().add_new_subscriber(sub, num))

    @staticmethod
    def get_all_subscribers():
        views.out_subscribers_and_their_phone_numbers(
            PhoneBook.get_object().get_all_subscribers_with_phone_numbers())

    @staticmethod
    def find_subscriber(key):
        value = enter_subscribers_data(key)
        views.out_subscribers_and_their_phone_numbers([
            PhoneBook.get_object().find_subscriber(key, value)])

    @staticmethod
    def update_subscriber(key):
        sub = PhoneBook.get_object().find_subscriber(
            key, enter_subscribers_data(key))
        res = -1
        if sub is not None:
            inv_key = 'subscriber' if key == 'phone' else 'phone'
            val = enter_subscribers_data(key)
            res = PhoneBook.get_object().update_subscriber(inv_key, sub, val)
            views.out_subscribers_and_their_phone_numbers([
                PhoneBook.get_object().find_subscriber(key, val)])
        views.print_result_of_updating(res)

    @staticmethod
    def delete_subscriber():
        value = enter_subscribers_data('subscriber')
        views.print_result_of_deleting(
            PhoneBook.get_object().remove_subscriber('subscriber', value))
        views.out_subscribers_and_their_phone_numbers(
            PhoneBook.get_object().get_all_subscribers_with_phone_numbers())

    @staticmethod
    def save_and_exit():
        PhoneBook.get_object().save_database()
        exit()
