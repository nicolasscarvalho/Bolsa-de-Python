from instruments_academy import PSU, Equity, Eload
from time import sleep

class Test:

    def __init__(self) -> None:
        self._id = 1000
        self._name = 'Load Transient'
        self._description = 'None'
        self._fm_state = 'START'
        self._fm_sleep_time = 0.1
        self._temperature_step = 0

    def _fm(self):
        
        if self._fm_state == 'START':
            
            # Importing modules
            self.psu = PSU()
            self.equity = Equity()
            self.eload = Eload()

            
            # Setting temperature list and a
            self._temperature = [-10, 25, 85]
            self._current_temperature = self._temperature[self._temperature_step]

            if not 0 <= self._current_temperature <= 60:
                raise ValueError('Temperature range error')
            

            # Setting stabilization temperature time
            self._stabilization_temperature_time = 40 * 60

            if not 0 <= self._stabilization_temperature_time <= 3600:
                raise ValueError('Stabilization temperature time range error')
            

            # Setting voltage C
            self._voltage_C = [0] 


            # Setting electronic charge

            # Initial electric current
            self._initial_electric_current = 3

            if not 0 <= self._initial_electric_current <= 5:
                raise ValueError('Initial electric current range error')
            
            assert type(self._initial_electric_current) is float

            # Final electric current
            self._final_electric_current = 6
            if not 1 <= self._initial_electric_current <= 10:
                raise ValueError('Final electric current range error')
            
            assert type(self._final_electric_current) is float
            

            # Setting voltage X
            self._voltage_X = 10