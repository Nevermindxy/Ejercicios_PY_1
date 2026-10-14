#PIDE LA NOTA FINAL DE UN ESTUDIANTE DE 0 A 100, SI EL PROMEDIO ES MENOR IGUAL A 50 MOSTRAR REPROBADO CON LA NOTA DE REPROBACION Y SI ES MAYOR IGUAL A 51 MOSTRAR APROBADO CON LA NOTA DE APROBACION
nota_final=int(input('introducir la nota final del estudiante(0 a 100)'))
if nota_final<=50:
    print(f"el estudiante con la nota {nota_final} REPROBO")
else:
    print(f"el estudiante con la nota {nota_final} APROBO")