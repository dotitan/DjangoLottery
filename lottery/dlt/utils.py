from .models import DLT, Tag


def create(request, count=5):
    num = Tag.objects.last().num

    for i in range(count):
        front = sorted(random.sample(range(1, 36), 5))
        back = sorted(random.sample(range(1, 13), 2))
        dlt = DLT.objects.create(owner=owner,
                                 a=front[0], 
                                 b=front[1],
                                 c=front[2],
                                 d=front[3],
                                 e=front[4],
                                 f=back[0],
                                 g=back[1],
                                 num=num)