#TUGAS 2

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

Informasi = ctrl.Antecedent(np.arange(0, 101, 1), 'info')
persyaratan = ctrl.Antecedent(np.arange(0, 101, 1), 'persyaratan')
petugas = ctrl.Antecedent(np.arange(0, 101, 1), 'petugas')
sarpras = ctrl.Antecedent(np.arange(0, 101, 1), 'sarpras')

pelayanan = ctrl.Consequent(np.arange(0, 401, 1), 'pelayanan')

Informasi['Tidak Puas'] = fuzz.trapmf(Informasi.universe, [0, 0, 60, 75])
Informasi['Cukup Puas'] = fuzz.trimf(Informasi.universe, [60, 75, 90])
Informasi['Puas'] = fuzz.trapmf(Informasi.universe, [75, 90, 100, 100])

persyaratan['Tidak Puas'] = fuzz.trapmf(persyaratan.universe, [0, 0, 60, 75])
persyaratan['Cukup Puas'] = fuzz.trimf(persyaratan.universe, [60, 75, 90])
persyaratan['Puas'] = fuzz.trapmf(persyaratan.universe, [75, 90, 100, 100])

petugas['Tidak Puas'] = fuzz.trapmf(petugas.universe, [0, 0, 60, 75])
petugas['Cukup Puas'] = fuzz.trimf(petugas.universe, [60, 75, 90])
petugas['Puas'] = fuzz.trapmf(petugas.universe, [75, 90, 100, 100 ])

sarpras['Tidak Puas'] = fuzz.trapmf(sarpras.universe, [0, 0, 60, 75])
sarpras['Cukup Puas'] = fuzz.trimf(sarpras.universe, [60, 75, 90])
sarpras['Puas'] = fuzz.trapmf(sarpras.universe, [75, 90, 100, 100])

pelayanan['Tidak Puas'] = fuzz.trapmf(pelayanan.universe, [0, 0, 50, 75])
pelayanan['Kurang Puas'] = fuzz.trapmf(pelayanan.universe, [50, 75, 100, 150])
pelayanan['cukup Puas'] = fuzz.trapmf(pelayanan.universe, [100, 150, 250, 275])
pelayanan['Puas'] = fuzz.trapmf(pelayanan.universe, [250, 275, 325, 350])
pelayanan['Sangat Puas'] = fuzz.trapmf(pelayanan.universe, [325, 350, 400, 400])

rule1 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Tidak Puas'] & petugas['Tidak Puas'] & sarpras['Tidak Puas'], pelayanan['Kurang Puas'])
rule2 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Tidak Puas'] & petugas['Tidak Puas'] & sarpras['Cukup Puas'], pelayanan['cukup Puas'])
rule3 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Tidak Puas'] & petugas['Tidak Puas'] & sarpras['Puas'], pelayanan['cukup Puas'])
rule4 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Tidak Puas'] & petugas['Cukup Puas'] & sarpras['Tidak Puas'], pelayanan['cukup Puas'])
rule5 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Tidak Puas'] & petugas['Cukup Puas'] & sarpras['Cukup Puas'], pelayanan['cukup Puas'])
rule6 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Tidak Puas'] & petugas['Cukup Puas'] & sarpras['Puas'], pelayanan['cukup Puas'])
rule7 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Tidak Puas'] & petugas['Puas'] & sarpras['Tidak Puas'], pelayanan['cukup Puas'])
rule8 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Tidak Puas'] & petugas['Puas'] & sarpras['Cukup Puas'], pelayanan['cukup Puas'])
rule9 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Tidak Puas'] & petugas['Puas'] & sarpras['Puas'], pelayanan['Puas'])
rule10 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Cukup Puas'] & petugas['Tidak Puas'] & sarpras['Tidak Puas'], pelayanan['cukup Puas'])
rule11 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Cukup Puas'] & petugas['Tidak Puas'] & sarpras['Cukup Puas'], pelayanan['cukup Puas'])
rule12 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Cukup Puas'] & petugas['Tidak Puas'] & sarpras['Puas'], pelayanan['cukup Puas'])
rule13 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Cukup Puas'] & petugas['Cukup Puas'] & sarpras['Tidak Puas'], pelayanan['cukup Puas'])
rule14 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Cukup Puas'] & petugas['Cukup Puas'] & sarpras['Cukup Puas'], pelayanan['cukup Puas'])
rule15 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Cukup Puas'] & petugas['Cukup Puas'] & sarpras['Puas'], pelayanan['Puas'])
rule16 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Cukup Puas'] & petugas['Puas'] & sarpras['Tidak Puas'], pelayanan['cukup Puas'])
rule17 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Cukup Puas'] & petugas['Puas'] & sarpras['Cukup Puas'], pelayanan['Puas'])
rule18 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Cukup Puas'] & petugas['Puas'] & sarpras['Puas'], pelayanan['Puas'])
rule19 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Puas'] & petugas['Tidak Puas'] & sarpras['Tidak Puas'], pelayanan['cukup Puas'])
rule20 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Puas'] & petugas['Tidak Puas'] & sarpras['Cukup Puas'], pelayanan['cukup Puas'])
rule21 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Puas'] & petugas['Tidak Puas'] & sarpras['Puas'], pelayanan['Puas'])
rule22 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Puas'] & petugas['Cukup Puas'] & sarpras['Tidak Puas'], pelayanan['cukup Puas'])
rule23 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Puas'] & petugas['Cukup Puas'] & sarpras['Cukup Puas'], pelayanan['Puas'])
rule24 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Puas'] & petugas['Cukup Puas'] & sarpras['Puas'], pelayanan['Puas'])
rule25 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Puas'] & petugas['Puas'] & sarpras['Tidak Puas'], pelayanan['Puas'])
rule26 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Puas'] & petugas['Puas'] & sarpras['Cukup Puas'], pelayanan['Puas'])
rule27 = ctrl.Rule(Informasi['Tidak Puas'] & persyaratan['Puas'] & petugas['Puas'] & sarpras['Puas'], pelayanan['Sangat Puas'])
rule28 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Tidak Puas'] & petugas['Tidak Puas'] & sarpras['Tidak Puas'], pelayanan['cukup Puas'])
rule29 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Tidak Puas'] & petugas['Tidak Puas'] & sarpras['Cukup Puas'], pelayanan['cukup Puas'])
rule30 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Tidak Puas'] & petugas['Tidak Puas'] & sarpras['Puas'], pelayanan['cukup Puas'])
rule31 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Tidak Puas'] & petugas['Cukup Puas'] & sarpras['Tidak Puas'], pelayanan['cukup Puas'])
rule32 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Tidak Puas'] & petugas['Cukup Puas'] & sarpras['Cukup Puas'], pelayanan['cukup Puas'])
rule33 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Tidak Puas'] & petugas['Cukup Puas'] & sarpras['Puas'], pelayanan['Puas'])
rule34 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Tidak Puas'] & petugas['Puas'] & sarpras['Tidak Puas'], pelayanan['cukup Puas'])
rule35 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Tidak Puas'] & petugas['Puas'] & sarpras['Cukup Puas'], pelayanan['Puas'])
rule36 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Tidak Puas'] & petugas['Puas'] & sarpras['Puas'], pelayanan['Puas'])
rule37 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Cukup Puas'] & petugas['Tidak Puas'] & sarpras['Tidak Puas'], pelayanan['cukup Puas'])
rule38 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Cukup Puas'] & petugas['Tidak Puas'] & sarpras['Cukup Puas'], pelayanan['cukup Puas'])
rule39 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Cukup Puas'] & petugas['Tidak Puas'] & sarpras['Puas'], pelayanan['Puas'])
rule40 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Cukup Puas'] & petugas['Cukup Puas'] & sarpras['Tidak Puas'], pelayanan['cukup Puas'])
rule41 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Cukup Puas'] & petugas['Cukup Puas'] & sarpras['Cukup Puas'], pelayanan['Puas'])
rule42 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Cukup Puas'] & petugas['Cukup Puas'] & sarpras['Puas'], pelayanan['Puas'])
rule43 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Cukup Puas'] & petugas['Puas'] & sarpras['Tidak Puas'], pelayanan['Puas'])
rule44 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Cukup Puas'] & petugas['Puas'] & sarpras['Cukup Puas'], pelayanan['Puas'])
rule45 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Cukup Puas'] & petugas['Puas'] & sarpras['Puas'], pelayanan['Sangat Puas'])

rule46 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Puas'] & petugas['Tidak Puas'] & sarpras['Tidak Puas'], pelayanan['cukup Puas'])
rule47 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Puas'] & petugas['Tidak Puas'] & sarpras['Cukup Puas'], pelayanan['Puas'])
rule48 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Puas'] & petugas['Tidak Puas'] & sarpras['Puas'], pelayanan['Puas'])
rule49 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Puas'] & petugas['Cukup Puas'] & sarpras['Tidak Puas'], pelayanan['Puas'])
rule50 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Puas'] & petugas['Cukup Puas'] & sarpras['Cukup Puas'], pelayanan['Puas'])
rule51 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Puas'] & petugas['Cukup Puas'] & sarpras['Puas'], pelayanan['Sangat Puas'])
rule52 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Puas'] & petugas['Puas'] & sarpras['Tidak Puas'], pelayanan['Puas'])
rule53 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Puas'] & petugas['Puas'] & sarpras['Cukup Puas'], pelayanan['Sangat Puas'])
rule54 = ctrl.Rule(Informasi['Cukup Puas'] & persyaratan['Puas'] & petugas['Puas'] & sarpras['Puas'], pelayanan['Sangat Puas'])

rule55 = ctrl.Rule(Informasi['Puas'] & persyaratan['Tidak Puas'] & petugas['Tidak Puas'] & sarpras['Tidak Puas'], pelayanan['cukup Puas'])
rule56 = ctrl.Rule(Informasi['Puas'] & persyaratan['Tidak Puas'] & petugas['Tidak Puas'] & sarpras['Cukup Puas'], pelayanan['cukup Puas'])
rule57 = ctrl.Rule(Informasi['Puas'] & persyaratan['Tidak Puas'] & petugas['Tidak Puas'] & sarpras['Puas'], pelayanan['Puas'])
rule58 = ctrl.Rule(Informasi['Puas'] & persyaratan['Tidak Puas'] & petugas['Cukup Puas'] & sarpras['Tidak Puas'], pelayanan['cukup Puas'])
rule59 = ctrl.Rule(Informasi['Puas'] & persyaratan['Tidak Puas'] & petugas['Cukup Puas'] & sarpras['Cukup Puas'], pelayanan['Puas'])
rule60 = ctrl.Rule(Informasi['Puas'] & persyaratan['Tidak Puas'] & petugas['Cukup Puas'] & sarpras['Puas'], pelayanan['Puas'])
rule61 = ctrl.Rule(Informasi['Puas'] & persyaratan['Tidak Puas'] & petugas['Puas'] & sarpras['Tidak Puas'], pelayanan['Puas'])
rule62 = ctrl.Rule(Informasi['Puas'] & persyaratan['Tidak Puas'] & petugas['Puas'] & sarpras['Cukup Puas'], pelayanan['Puas'])
rule63 = ctrl.Rule(Informasi['Puas'] & persyaratan['Tidak Puas'] & petugas['Puas'] & sarpras['Puas'], pelayanan['Sangat Puas'])

rule64 = ctrl.Rule(Informasi['Puas'] & persyaratan['Cukup Puas'] & petugas['Tidak Puas'] & sarpras['Tidak Puas'], pelayanan['cukup Puas'])
rule65 = ctrl.Rule(Informasi['Puas'] & persyaratan['Cukup Puas'] & petugas['Tidak Puas'] & sarpras['Cukup Puas'], pelayanan['Puas'])
rule66 = ctrl.Rule(Informasi['Puas'] & persyaratan['Cukup Puas'] & petugas['Tidak Puas'] & sarpras['Puas'], pelayanan['Puas'])
rule67 = ctrl.Rule(Informasi['Puas'] & persyaratan['Cukup Puas'] & petugas['Cukup Puas'] & sarpras['Tidak Puas'], pelayanan['Puas'])
rule68 = ctrl.Rule(Informasi['Puas'] & persyaratan['Cukup Puas'] & petugas['Cukup Puas'] & sarpras['Cukup Puas'], pelayanan['Puas'])
rule69 = ctrl.Rule(Informasi['Puas'] & persyaratan['Cukup Puas'] & petugas['Cukup Puas'] & sarpras['Puas'], pelayanan['Sangat Puas'])
rule70 = ctrl.Rule(Informasi['Puas'] & persyaratan['Cukup Puas'] & petugas['Puas'] & sarpras['Tidak Puas'], pelayanan['Puas'])
rule71 = ctrl.Rule(Informasi['Puas'] & persyaratan['Cukup Puas'] & petugas['Puas'] & sarpras['Cukup Puas'], pelayanan['Sangat Puas'])
rule72 = ctrl.Rule(Informasi['Puas'] & persyaratan['Cukup Puas'] & petugas['Puas'] & sarpras['Puas'], pelayanan['Sangat Puas'])

rule73 = ctrl.Rule(Informasi['Puas'] & persyaratan['Puas'] & petugas['Tidak Puas'] & sarpras['Tidak Puas'], pelayanan['Puas'])
rule74 = ctrl.Rule(Informasi['Puas'] & persyaratan['Puas'] & petugas['Tidak Puas'] & sarpras['Cukup Puas'], pelayanan['Puas'])
rule75 = ctrl.Rule(Informasi['Puas'] & persyaratan['Puas'] & petugas['Tidak Puas'] & sarpras['Puas'], pelayanan['Sangat Puas'])
rule76 = ctrl.Rule(Informasi['Puas'] & persyaratan['Puas'] & petugas['Cukup Puas'] & sarpras['Tidak Puas'], pelayanan['Puas'])
rule77 = ctrl.Rule(Informasi['Puas'] & persyaratan['Puas'] & petugas['Cukup Puas'] & sarpras['Cukup Puas'], pelayanan['Sangat Puas'])
rule78 = ctrl.Rule(Informasi['Puas'] & persyaratan['Puas'] & petugas['Cukup Puas'] & sarpras['Puas'], pelayanan['Sangat Puas'])
rule79 = ctrl.Rule(Informasi['Puas'] & persyaratan['Puas'] & petugas['Puas'] & sarpras['Tidak Puas'], pelayanan['Sangat Puas'])
rule80 = ctrl.Rule(Informasi['Puas'] & persyaratan['Puas'] & petugas['Puas'] & sarpras['Cukup Puas'], pelayanan['Sangat Puas'])
rule81 = ctrl.Rule(Informasi['Puas'] & persyaratan['Puas'] & petugas['Puas'] & sarpras['Puas'], pelayanan['Sangat Puas'])

stok_ctrl = ctrl.ControlSystem([
    rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
    rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18,
    rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27,
    rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36,
    rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45,
    rule46, rule47, rule48, rule49, rule50, rule51, rule52, rule53, rule54,
    rule55, rule56, rule57, rule58, rule59, rule60, rule61, rule62, rule63,
    rule64, rule65, rule66, rule67, rule68, rule69, rule70, rule71, rule72,
    rule73, rule74, rule75, rule76, rule77, rule78, rule79, rule80, rule81
])
pelayanan_simulation = ctrl.ControlSystemSimulation(stok_ctrl)


input_info = 80 
input_persyaratan = 60 
input_petugas = 50 
input_sarpras = 90 

pelayanan_simulation.input['info'] = input_info
pelayanan_simulation.input['persyaratan'] = input_persyaratan
pelayanan_simulation.input['petugas'] = input_petugas
pelayanan_simulation.input['sarpras'] = input_sarpras

pelayanan_simulation.compute()

hasil_pelayanan = pelayanan_simulation.output['pelayanan']
print("--- HASIL PERHITUNGAN LOGIKA FUZZY ---")
print(f"Kejelasan Informasi     : {input_info}")
print(f"Kejelasan Persyaratan   : {input_persyaratan}")
print(f"Kemampuan Petugas       : {input_petugas}")
print(f"Ketersediaan Sarpras    : {input_sarpras}")
print("--------------------------------------")
print(f"Kepuasan Pelayanan yang Direkomendasikan: {hasil_pelayanan:.2f}")

Informasi.view(sim=pelayanan_simulation)
persyaratan.view(sim=pelayanan_simulation)
petugas.view(sim=pelayanan_simulation)
sarpras.view(sim=pelayanan_simulation)
pelayanan.view(sim=pelayanan_simulation)