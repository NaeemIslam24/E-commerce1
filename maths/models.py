from django.db import models

# Create your models here.


class Math_type(models.Model):

    sign = models.CharField(max_length=50)

    def __str__(self):
        return self.sign


class Math(models.Model):

    number1 = models.FloatField(default=0)
    number2 = models.FloatField(default=0)
    add_sign = models.OneToOneField(
        Math_type,  on_delete=models.SET_NULL, null=True)

    def get_total(self):

        if '+' == self.add_sign.sign:  # self.add_sign to Math_type app's sign

            total = self.number1+self.number2
            return total

        elif '-' == self.add_sign.sign:  # self.add_sign to Math_type app's sign

            total = self.number1-self.number2
            return total

        elif '*' == self.add_sign.sign:  # self.add_sign to Math_type app's sign

            total = self.number1*self.number2
            return total

        elif '/' == self.add_sign.sign:  # self.add_sign to Math_type app's sign

            total = self.number1/self.number2
            return total
