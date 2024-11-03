from random import randint
import requests
from datetime import datetime, timedelta

class Pokemon:
    pokemons = {}

    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):


        self.pokemon_trainer = pokemon_trainer


        self.last_feed_time = datetime


        self.hp = randint(100,1000)
        self.power = randint(100,1000)
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        

        Pokemon.pokemons[pokemon_trainer] = self


    def feed(self, feed_interval = 20, hp_increase = 100):
        current_time = datetime.now()  
        delta_time = timedelta(second=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {current_time+delta_time}"


    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/1.png"
    

    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
    

    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        else:
            if enemy.hp > self.power:
                enemy.hp -= self.power
                return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
            else:
                enemy.hp = 0
                return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
            

    # Метод класса для получения информации
    def info(self):
        
        return f"""Имя твоего покеомона: {self.name}. 
        Здоровье: {self.hp}.
        Сила: {self.power}."""


    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img


class Wizard(Pokemon):
    def info(self):
        return f"У тебя покемон волшебник. \n" +super().info()
        

    def feed(self):
        return super().feed(feed_interval = 10, hp_increase = 100)
    

    def attack(self, enemy):
        return super().attack(enemy)


class Fighter(Pokemon):
    def info(self):
        return f"У тебя покемон боец. \n" +super().info()
        
    
    def feed(self):
        return super().feed(feed_interval = 20, hp_increase = 200)


    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\nБоец применил супер-атаку силой:{super_power}"
    

if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")


    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))