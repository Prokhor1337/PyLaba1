class Character:
   def __init__(self, name, level=0, hp=0, attack=0):
       self.name = name
       self.level = level
       self.hp = hp
       self.attack = attack


   def display(self):
       print(f"Ім'я: {self.name}, Рівень: {self.level}, Здоров'я: {self.hp}, Атака: {self.attack}")


   def attack_the_enemy(self, enemy):
       if self.attack > 0:
           print(f"{self.name} атакує {enemy.name}!")
           enemy.hp -= self.attack
           if enemy.hp <= 0:
               enemy.hp = 0
               print(f"{enemy.name} переможений!")
           else:
               print(f"Здоров'я {enemy.name} зменшилося на {self.attack}.")
               print(f"Здоров'я {enemy.name}: {enemy.hp}")
       else:
           print("Сила атаки має бути більшою за нуль.")


   def heal(self, amount):
       if amount > 0:
           self.hp += amount
           print(f"{self.name} відновив {amount} здоров'я. Поточне здоров'я: {self.hp}")
       else:
           print("Значення відновлення здоров'я має бути більшим за нуль.")




class Warrior(Character):
   def __init__(self, name, level=0, hp=0, attack=0, armor=0):
       super().__init__(name, level, hp, attack)
       self.armor = armor


   def display(self):
       super().display()
       print(f"Броня: {self.armor}")




class Mage(Character):
   def __init__(self, name, level=0, hp=0, attack=0, mana=10):
       super().__init__(name, level, hp, attack)
       self.mana = mana


   def display(self):
       super().display()
       print(f"Мана: {self.mana}")


   def cast_spell(self, enemy):
       if self.mana > 0:
           print(f"{self.name} кидає закляття в {enemy.name}!")
           enemy.hp -= self.attack
           self.mana -= 1


           if enemy.hp <= 0:
               enemy.hp = 0
               print(f"{enemy.name} переможений закляттям!")
           else:
               print(f"{enemy.name} отримав {self.attack} шкоди. Залишилось {enemy.hp} здоров'я.")


           print(f"Залишок мани: {self.mana}")
       else:
           print("Немає мани для закляття!")




class Archer(Character):
   def __init__(self, name, level=0, hp=0, attack=0, arrows=10):
       super().__init__(name, level, hp, attack)
       self.arrows = arrows


   def display(self):
       super().display()
       print(f"Кількість стріл: {self.arrows}")


   def shoot_arrow(self, enemy):
       if self.arrows > 0:
           print(f"{self.name} стріляє стрілу в {enemy.name}!")
           enemy.hp -= self.attack
           self.arrows -= 1
           if enemy.hp <= 0:
               enemy.hp = 0
               print(f"{enemy.name} переможений стрілою!")
           else:
               print(f"{enemy.name} отримав {self.attack} шкоди. Залишилось {enemy.hp} здоров'я.")
           print(f"Залишилось стріл: {self.arrows}")
       else:
           print("Немає стріл!")




hero = Warrior("Герой", 5, 100, 20, armor=15)
mage = Mage("Маг", 4, 70, 15, mana=50)
archer = Archer("Лучник", 4, 80, 18, arrows=5)
enemy = Character("Лиходій", 3, 60, 12)


hero.display()
mage.display()
archer.display()
enemy.display()


print("\nБій:")
archer.shoot_arrow(enemy)
mage.cast_spell(enemy)
hero.attack_the_enemy(enemy)


print("\nВідновлення:")
hero.heal(20)
mage.heal(15)
archer.heal(10)
