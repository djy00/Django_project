from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    year = models.IntegerField(default=1900)
    
    def __str__(self):
        return f"{self.brand}_{self.model}_{self.color}_{self.year}"

    class Meta:
        ordering = ['-year']    #정렬 기준?

class Inventory(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    number = models.IntegerField(default=1900)


'''
model meta option
- abstract = True
해당 모델이 추상 클래스임을 의미. => DB에 테이블로 생성 X, 다른 모델들이 이 클래스를 상속받아 필드나 메서드를 공유할 수 있게 함
=> 이를 상속하는 하위 모델들이 공통된 속성을 가지게함
ex)여러 모델에 공통으로 들어가는 필드들이 있을 때, 추상 클래스를 만들어 각 모델에서 상속받아 사용할 수 있음

- bd_table = 'music_album'
테이블 이름을 따로 짓고싶을때 사용

- get_latest_by = "order_date"
어떤 필드를 중심으로 리턴할건지 정함

- managed = True
True가 디폴트, False를 쓰면 migration을 해도 해당 테이블을 메니징 하지않음

- ordering = ['-order_date']
정렬 기준

- indexes

- unique_together=[]
unique값을 지정할 수 있음

- index_together=[[]]
위와 비슷

- verbose_name = ""
테이블을 읽을 때 어떻게 읽은지

- verbose_name_plural = "stories"

'''
    