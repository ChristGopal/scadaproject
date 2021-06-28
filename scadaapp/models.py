from django.db import models

# Create your models here.


class Datalog(models.Model):
    opc_iot_cheff_value = models.FloatField(db_column='OPC_IOT_CHEFF_VALUE', blank=True,
                                            null=True)  # Field name made lowercase.
    opc_iot_energy_value = models.FloatField(db_column='OPC_IOT_ENERGY_VALUE', blank=True,
                                             null=True)  # Field name made lowercase.
    opc_iot_flow_value = models.FloatField(db_column='OPC_IOT_FLOW_VALUE', blank=True,
                                           null=True)  # Field name made lowercase.
    opc_iot_flow_timestamp = models.DateTimeField(db_column='OPC_IOT_FLOW_TIMESTAMP', blank=True,
                                                  null=True)  # Field name made lowercase.
    opc_iot_level_value = models.FloatField(db_column='OPC_IOT_LEVEL_VALUE', blank=True,
                                            null=True)  # Field name made lowercase.
    opc_iot_press_value = models.FloatField(db_column='OPC_IOT_PRESS_VALUE', blank=True,
                                            null=True)  # Field name made lowercase.
    opc_iot_temp_value = models.FloatField(db_column='OPC_IOT_TEMP_VALUE', blank=True,
                                           null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'datalog'