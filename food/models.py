from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Item(models.Model):
    
    def __str__(self):
        return self.item_name
    
    user_name = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_prce = models.IntegerField()
    item_image = models.CharField(max_length=500,default='https://www.google.com/search?q=placeholder+food+images&client=ubuntu&channel=fs&tbm=isch&source=iu&ictx=1&vet=1&fir=r4MyYWa6UxepTM%252CDE59x2KNdrhkvM%252C_%253Bjal7CZrCohPPcM%252CSht218MD2XkntM%252C_%253B7K26ALkHdMGaaM%252CpW-HFWw0VNMbnM%252C_%253BcAtq_o3hdy3hOM%252CPAwBzaJSiNcWRM%252C_%253Bi4LWV8nsfF3pZM%252Cvm_HY1Gpe19S-M%252C_%253BKzlEw1u98W7EKM%252C75wDOX_EasD4oM%252C_%253B59Y8go7tPpJqKM%252C0k5rhoJHXvlkdM%252C_%253BbrvVOAlrbLzfVM%252CwjWTBq_jYqmdeM%252C_%253B_f-j934pbgJPIM%252Ce1j17iealMc86M%252C_%253B-fO_excvO9BrdM%252C0RuYXFRXZuB68M%252C_%253B3gu7rag2AQnNmM%252C7RPpozL6R3FwOM%252C_%253BtWHGFraLIpPmbM%252C-EYq4YMSSYYZMM%252C_%253BFqgiTtdteGma4M%252CNhlb63xefFds-M%252C_%253B5nsC28LDwnHlEM%252CDTuB0awS6s_LNM%252C_&usg=AI4_-kS4Uy0trVJ_UU2EfRNF_SnuhXfZKQ&sa=X&ved=2ahUKEwiA8ougu_T3AhWP7XMBHSb5CT0Q9QF6BAgDEAE#imgrc=r4MyYWa6UxepTM')