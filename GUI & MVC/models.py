# coding: utf-8
"""
    author: Louai KASSA BAGHDOUCHE

"""

import csv
import os

class Person:
    """Model class"""

    def __init__(self, name, last_name, phone, adresse, city):
        """Constructor

        Args:
            name (str): name of the person
            last_name (str): last name of the person
            phone (str): phone number
            adresse (str): adresse
            city (str): city
        """
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.adresse = adresse
        self.city = city

        if not os.path.exists('individus.tsv'):
            with open('individus.tsv', 'w') as tsv_file:
                fields = ['name', 'last_name', 'phone', 'adresse', 'city']
                writer = csv.DictWriter(tsv_file, fieldnames=fields, delimiter='\t')
                writer.writeheader()

    def __str__(self):
        """string method to discribe the object

        Returns:
            string description of the object
        """
        return "Hello there! My name is %s %s, my phone number is %s and i'm living in %s at %s" % (
            self.name,
            self.last_name,
            self.phone,
            self.city,
            self.adresse
        )

    def insert_to_file(self):
        """Model of our tsv file which stores all of the informations.

        If the persons.tsv file doesn't exist we will create it and initialize it
        with fields (name, last name ...)

        If it already exists we will open it with the append format 'a' to add informations
        """

        with open('individus.tsv', 'a') as tsv_file:
            writer = csv.writer(tsv_file, delimiter='\t')
            writer.writerow([self.name, self.last_name, self.phone, self.adresse, self.city])

    def already_exists(self):
        """this method checks wether an inputed person exists in the tsv file or not

        Returns:
            boolean
        """

        response = False

        with open('individus.tsv', 'r') as tsv_file:
            lines = csv.DictReader(tsv_file, delimiter='\t')
            for line in lines:
                if self.name == line['name'] and self.last_name == line['last_name']:
                    response = True
                    break

        return response

    @staticmethod
    def search_person(name):
        """static method to search by name the informations of the person

        Args:
            name (string): the person's name

        Returns:
            tuple: counter is the number of the results, and a string contains all the informations
        """
        results = ''
        counter = 0
        with open('individus.tsv', 'r') as tsv_file:
            lines = csv.DictReader(tsv_file, delimiter='\t')
            for line in lines:
                if name == line['name']:
                    results += '\nName : %s %s\nPhone: %s\nAdresse \
                        and city: %s %s\n-------------' % (
                            line['name'],
                            line['last_name'],
                            line['phone'],
                            line['adresse'],
                            line['city'])
                    counter += 1

        return (results, counter)
