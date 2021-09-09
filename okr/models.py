from django.db import models

class Objective(models.Model):

    title = models.CharField(max_length=60)
    parent_key_result = models.OneToOneField("KeyResult", related_name="derived_objective", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return "Objective(pk={}, title={}, parent_key_result={})".format(
            self.pk, 
            self.title, 
            str(self.parent_key_result)
        )

class KeyResult(models.Model):

    title = models.CharField(max_length=100)
    objective = models.ForeignKey("Objective", related_name="key_results", on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return "KeyResult(pk={}, title={}, objective={})".format(
            self.pk, 
            self.title,
            str(self.objective)
        )

    