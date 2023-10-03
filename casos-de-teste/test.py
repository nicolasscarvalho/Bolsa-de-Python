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


            # Setting functions
            self._config_eload()
            self._config_equity()
            self._config_psu()

            
            # Setting temperature list and a
            self._temperature = [-10.0, 25.0, 85.0]
            self._current_temperature = self._temperature[self._temperature_step]

            if not 0 <= self._current_temperature <= 60:
                raise ValueError('Temperature range error')
            

            # Setting stabilization temperature time
            self._stabilization_temperature_time = 40 * 60

            if not 0 <= self._stabilization_temperature_time <= 3600:
                raise ValueError('Stabilization temperature time range error')
            

            # Setting voltage C
            self._voltage_C = [0.0] 


            # Setting electronic charge

            # Initial electric current
            self._initial_electric_current = 3.0

            if not 0 <= self._initial_electric_current <= 5:
                raise ValueError('Initial electric current range error')
            
            assert type(self._initial_electric_current) is float

            # Final electric current
            self._final_electric_current = 6.0
            if not 1 <= self._initial_electric_current <= 10:
                raise ValueError('Final electric current range error')
            
            assert type(self._final_electric_current) is float
            

            # Setting voltage X
            self._voltage_X = 120.0


            self.eload.write(f'VOLT f{self._voltage_C}')

            self._fm_state = 'CONFIG_EQUITY'


        elif self._fm_state == 'CONFIG_EQUITY':
            # Setting actual current
            self._actual_electric_current = self._initial_electric_current

            self.equity.set_temperature(self._current_temperature)

            while self._current_temperature != self.equity.get_temperature():
                sleep(1)
            
            #sleep(self._stabilization_temperature_time)

            self._fm_state = 'CONFIG_PSU'


        elif self._fm_state == 'CONFIG_PSU':
            self._fm_state = 'CONFIG_ELECTRONIC_CHARGE'

            self.psu.set_voltage(self._voltage_X)
            sleep(1)

            self._fm_state = 'CONFIG_ELOAD'


        elif self._fm_state == 'CONFIG_ELOAD':
            self.eload.write(f'CURR {self._actual_electric_current}')
            sleep(1)
            self._fm_state = 'SHOW_OUTPUT'

        
        elif self._fm_state == 'SHOW_OUTPUT':
            self._output_power = float(self.eload.query("MEAS:POW?"))

            print(f'ELOAD Actual electric current: f{self.eload.query("MEAS:CURR?")}')
            print(f'ELOAD Actual electric voltage: f{self.eload.query("MEAS:VOLT?")}')

            print(f'PSU Actual electric current: f{self.psu.get_current()}')
            print(f'PSU Actual electric voltage: f{self.psu.get_voltage()}')

            print(f'ELOAD Actual electric voltage: f{self.output_power}')

            if self._output_power >= self._voltage_X:
                self._fm_state = 'END'
            else:
                self._fm_state = 'CONFIG_ELOAD'

        elif self._fm_state == 'VERIFY_TEMPERATURE_STEP':
            self._temperature_step += 1
            if self._temperature_step < len(self._temperature):
                self._current_temperature = self._temperature[self._temperature_step]
            else:
                self._fm_state = 'END'

        elif self._fm_state == 'END':
            self.psu.set_voltage(0)
            self.eload.write('CURR 0')
            self.eload.write('VOLT 0')
            self._stop_flag = True
        
        else:
            raise Exception('Invalid FM state')

    def _config_eload(self):
        self.eload.write('CURR 0')

    def _config_equity(self):
        self.equity.set_temperature(25.0)

    def _config_psu(self):
        self.psu.set_voltage(0.0)

    def _generate_report(self):
        pass

    def _main(self):
        self._stop_flag = False
        while self._stop_flag is False:
            self._fm()
            sleep(self._fm_sleep_time)
        print('Test is done')


sla = Test()
sla._main()