# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 20:58:47 2022

@author: Usuario
"""

import numpy as np

# pesos dos criterios, calculados pelo Fuzzy-AHP
w = [np.array([0.15220673, 0.21135029, 0.29029343]),
 np.array([0.04987939, 0.07575599, 0.11666039]),
 np.array([0.01684299, 0.02464865, 0.03671085]),
 np.array([0.04307587, 0.06912029, 0.1078242 ]),
 np.array([0.0805491 , 0.12080869, 0.18168591]),
 np.array([0.00199768, 0.00364318, 0.00701966]),
 np.array([0.01069283, 0.01959538, 0.03641615]),
 np.array([0.01416464, 0.02187607, 0.03450867]),
 np.array([0.05260166, 0.07879169, 0.11672011]),
 np.array([0.18963417, 0.2531111 , 0.33825357]),
 np.array([0.03152444, 0.04770164, 0.0714083 ]),
 np.array([0.03246444, 0.05268398, 0.08346974]),
 np.array([0.01297616, 0.02091305, 0.03314937])]

# Matrizes fuzzy de decisao, para cada especialista.
D1 = np.array([[[42, 42, 42],[27714.01, 27714.01, 27714.01],[8462.43, 8462.43, 8462.43],[16.62, 16.62, 16.62],[3, 5, 7],[3, 5, 7],[1, 3, 5],[1, 1, 3],[5, 7, 9],[1, 3, 5],[1, 3, 5],[1, 3, 5],[1, 1, 3]],[[48, 48, 48],[131675.11, 131675.11, 131675.11],[36371.02, 36371.02, 36371.02],[980.63, 980.63, 980.63],[3, 5, 7],[5, 7, 9],[3, 5, 7],[5, 7, 9],[5, 7, 9],[3, 5, 7],[3, 5, 7],[7, 9, 9],[1, 3, 5]],[[41, 41, 41],[19675.39, 19675.39, 19675.39],[6030.05, 6030.05, 6030.05],[7.18, 7.18, 7.18],[1, 3, 5],[1, 1, 3],[1, 1, 3],[1, 1, 3],[5, 7, 9],[5, 7, 9],[3, 5, 7],[7, 9, 9],[5, 7, 9]],[[38, 38, 38],[32129.74, 32129.74, 32129.74],[9471.81, 9471.81, 9471.81],[58.93, 58.93, 58.93],[5, 7, 9],[3, 5, 7],[5, 7, 9],[1, 3, 5],[3, 5, 7],[5, 7, 9],[7, 9, 9],[3, 5, 7],[5, 7, 9]],[[44, 44, 44],[59582.77, 59582.77, 59582.77],[18602.53, 18602.53, 18602.53],[517.28, 517.28, 517.28],[3, 5, 7],[5, 7, 9],[1, 3, 5],[5, 7, 9],[5, 7, 9],[3, 5, 7],[3, 5, 7],[5, 7, 9],[7, 9, 9]],[[37, 37, 37],[29288.02, 29288.02, 29288.02],[8489.24, 8489.24, 8489.24],[145.06, 145.06, 145.06],[1, 3, 5],[1, 1, 3],[3, 5, 7],[1, 3, 5],[3, 5, 7],[1, 3, 5],[1, 3, 5],[1, 3, 5],[1, 3, 5]],[[36, 36, 36],[34417.54, 34417.54, 34417.54],[9278.56, 9278.56, 9278.56],[417.5, 417.5, 417.5],[1, 3, 5],[1, 1, 3],[5, 7, 9],[3, 5, 7],[1, 3, 5],[1, 3, 5],[1, 3, 5],[1, 3, 5],[1, 3, 5]],[[41, 41, 41],[3021.99, 3021.99, 3021.99],[656.62, 656.62, 656.62],[6.96, 6.96, 6.96],[1, 1, 3],[1, 1, 3],[1, 3, 5],[1, 1, 3],[5, 7, 9],[1, 3, 5],[1, 3, 5],[7, 9, 9],[7, 9, 9]],[[41, 41, 41],[27270.65, 27270.65, 27270.65],[7819.06, 7819.06, 7819.06],[37.98, 37.98, 37.98],[1, 3, 5],[1, 3, 5],[7, 9, 9],[1, 1, 3],[1, 1, 3],[5, 7, 9],[1, 3, 5],[7, 9, 9],[3, 5, 7]],[[37, 37, 37],[30293.3, 30293.3, 30293.3],[10473.59, 10473.59, 10473.59],[46.68, 46.68, 46.68],[3, 5, 7],[1, 3, 5],[7, 9, 9],[1, 3, 5],[1, 1, 3],[5, 7, 9],[5, 7, 9],[3, 5, 7],[5, 7, 9]],[[37, 37, 37],[22933.38, 22933.38, 22933.38],[7516.61, 7516.61, 7516.61],[23.43, 23.43, 23.43],[1, 1, 3],[1, 3, 5],[1, 1, 3],[1, 1, 3],[7, 9, 9],[3, 5, 7],[1, 3, 5],[3, 5, 7],[3, 5, 7]],[[37, 37, 37],[25541.16, 25541.16, 25541.16],[7371.99, 7371.99, 7371.99],[22.34, 22.34, 22.34],[3, 5, 7],[1, 3, 5],[7, 9, 9],[1, 1, 3],[1, 1, 3],[5, 7, 9],[5, 7, 9],[3, 5, 7],[5, 7, 9]],[[37, 37, 37],[15379.51, 15379.51, 15379.51],[4589.9, 4589.9, 4589.9],[16.57, 16.57, 16.57],[1, 1, 3],[1, 1, 3],[1, 1, 3],[1, 1, 3],[5, 7, 9],[1, 3, 5],[1, 3, 5],[3, 5, 7],[3, 5, 7]],[[42, 42, 42],[29946.62, 29946.62, 29946.62],[9774.62, 9774.62, 9774.62],[32.49, 32.49, 32.49],[1, 3, 5],[1, 1, 3],[1, 3, 5],[1, 1, 3],[5, 7, 9],[5, 7, 9],[3, 5, 7],[3, 5, 7],[5, 7, 9]],[[42, 42, 42],[15348.01, 15348.01, 15348.01],[5529.99, 5529.99, 5529.99],[8.83, 8.83, 8.83],[1, 3, 5],[1, 1, 3],[1, 3, 5],[1, 1, 3],[5, 7, 9],[1, 3, 5],[1, 3, 5],[3, 5, 7],[5, 7, 9]],[[41, 41, 41],[37147.04, 37147.04, 37147.04],[11161.34, 11161.34, 11161.34],[158.17, 158.17, 158.17],[5, 7, 9],[1, 3, 5],[5, 7, 9],[1, 3, 5],[1, 3, 5],[3, 5, 7],[1, 3, 5],[5, 7, 9],[3, 5, 7]],[[42, 42, 42],[19779.39, 19779.39, 19779.39],[6829.25, 6829.25, 6829.25],[11.9, 11.9, 11.9],[1, 3, 5],[1, 3, 5],[1, 3, 5],[1, 1, 3],[5, 7, 9],[1, 3, 5],[1, 3, 5],[1, 3, 5],[1, 1, 3]]])
D2 = np.array([[[42, 42, 42],[27714.01, 27714.01, 27714.01],[8462.43, 8462.43, 8462.43],[16.62, 16.62, 16.62],[1, 1, 3],[1, 1, 3],[1, 1, 3],[1, 1, 3],[3, 5, 7],[3, 5, 7],[5, 7, 9],[7, 9, 9],[5, 7, 9]],[[48, 48, 48],[131675.11, 131675.11, 131675.11],[36371.02, 36371.02, 36371.02],[980.63, 980.63, 980.63],[1, 3, 5],[1, 3, 5],[1, 3, 5],[5, 7, 9],[5, 7, 9],[7, 9, 9],[7, 9, 9],[7, 9, 9],[3, 5, 7]],[[41, 41, 41],[19675.39, 19675.39, 19675.39],[6030.05, 6030.05, 6030.05],[7.18, 7.18, 7.18],[1, 1, 3],[1, 1, 3],[1, 1, 3],[1, 1, 3],[5, 7, 9],[7, 9, 9],[7, 9, 9],[7, 9, 9],[3, 5, 7]],[[38, 38, 38],[32129.74, 32129.74, 32129.74],[9471.81, 9471.81, 9471.81],[58.93, 58.93, 58.93],[1, 3, 5],[1, 3, 5],[1, 3, 5],[3, 5, 7],[3, 5, 7],[3, 5, 7],[5, 7, 9],[7, 9, 9],[5, 7, 9]],[[44, 44, 44],[59582.77, 59582.77, 59582.77],[18602.53, 18602.53, 18602.53],[517.28, 517.28, 517.28],[3, 5, 7],[3, 5, 7],[1, 3, 5],[5, 7, 9],[3, 5, 7],[3, 5, 7],[5, 7, 9],[7, 9, 9],[5, 7, 9]],[[37, 37, 37],[29288.02, 29288.02, 29288.02],[8489.24, 8489.24, 8489.24],[145.06, 145.06, 145.06],[1, 3, 5],[1, 3, 5],[1, 3, 5],[3, 5, 7],[3, 5, 7],[3, 5, 7],[5, 7, 9],[7, 9, 9],[5, 7, 9]],[[36, 36, 36],[34417.54, 34417.54, 34417.54],[9278.56, 9278.56, 9278.56],[417.5, 417.5, 417.5],[3, 5, 7],[1, 3, 5],[1, 3, 5],[5, 7, 9],[1, 3, 5],[3, 5, 7],[5, 7, 9],[7, 9, 9],[5, 7, 9]],[[41, 41, 41],[3021.99, 3021.99, 3021.99],[656.62, 656.62, 656.62],[6.96, 6.96, 6.96],[1, 1, 3],[1, 1, 3],[1, 1, 3],[1, 1, 3],[7, 9, 9],[3, 5, 7],[7, 9, 9],[7, 9, 9],[5, 7, 9]],[[41, 41, 41],[27270.65, 27270.65, 27270.65],[7819.06, 7819.06, 7819.06],[37.98, 37.98, 37.98],[1, 3, 5],[1, 1, 3],[1, 3, 5],[1, 3, 5],[3, 5, 7],[7, 9, 9],[7, 9, 9],[7, 9, 9],[3, 5, 7]],[[37, 37, 37],[30293.3, 30293.3, 30293.3],[10473.59, 10473.59, 10473.59],[46.68, 46.68, 46.68],[1, 3, 5],[1, 1, 3],[1, 3, 5],[1, 3, 5],[3, 5, 7],[3, 5, 7],[5, 7, 9],[7, 9, 9],[5, 7, 9]],[[37, 37, 37],[22933.38, 22933.38, 22933.38],[7516.61, 7516.61, 7516.61],[23.43, 23.43, 23.43],[1, 1, 3],[1, 1, 3],[1, 3, 5],[1, 3, 5],[3, 5, 7],[3, 5, 7],[5, 7, 9],[7, 9, 9],[5, 7, 9]],[[37, 37, 37],[25541.16, 25541.16, 25541.16],[7371.99, 7371.99, 7371.99],[22.34, 22.34, 22.34],[1, 1, 3],[1, 1, 3],[1, 3, 5],[1, 3, 5],[3, 5, 7],[3, 5, 7],[5, 7, 9],[7, 9, 9],[5, 7, 9]],[[37, 37, 37],[15379.51, 15379.51, 15379.51],[4589.9, 4589.9, 4589.9],[16.57, 16.57, 16.57],[1, 1, 3],[1, 1, 3],[1, 3, 5],[1, 1, 3],[3, 5, 7],[3, 5, 7],[5, 7, 9],[7, 9, 9],[5, 7, 9]],[[42, 42, 42],[29946.62, 29946.62, 29946.62],[9774.62, 9774.62, 9774.62],[32.49, 32.49, 32.49],[3, 5, 7],[3, 5, 7],[1, 3, 5],[1, 3, 5],[3, 5, 7],[3, 5, 7],[5, 7, 9],[7, 9, 9],[5, 7, 9]],[[42, 42, 42],[15348.01, 15348.01, 15348.01],[5529.99, 5529.99, 5529.99],[8.83, 8.83, 8.83],[1, 3, 5],[1, 1, 3],[1, 3, 5],[1, 3, 5],[3, 5, 7],[3, 5, 7],[5, 7, 9],[7, 9, 9],[5, 7, 9]],[[41, 41, 41],[37147.04, 37147.04, 37147.04],[11161.34, 11161.34, 11161.34],[158.17, 158.17, 158.17],[5, 7, 9],[3, 5, 7],[1, 3, 5],[3, 5, 7],[3, 5, 7],[7, 9, 9],[7, 9, 9],[7, 9, 9],[7, 9, 9]],[[42, 42, 42],[19779.39, 19779.39, 19779.39],[6829.25, 6829.25, 6829.25],[11.9, 11.9, 11.9],[3, 5, 7],[1, 3, 5],[1, 3, 5],[3, 5, 7],[3, 5, 7],[7, 9, 9],[7, 9, 9],[7, 9, 9],[7, 9, 9]]])
D3 = np.array([[[42, 42, 42],[27714.01, 27714.01, 27714.01],[8462.43, 8462.43, 8462.43],[16.62, 16.62, 16.62],[1, 3, 5],[5, 7, 9],[1, 3, 5],[1, 1, 3],[5, 7, 9],[3, 5, 7],[7, 9, 9],[7, 9, 9],[5, 7, 9]],[[48, 48, 48],[131675.11, 131675.11, 131675.11],[36371.02, 36371.02, 36371.02],[980.63, 980.63, 980.63],[3, 5, 7],[3, 5, 7],[1, 3, 5],[3, 5, 7],[5, 7, 9],[3, 5, 7],[5, 7, 9],[5, 7, 9],[5, 7, 9]],[[41, 41, 41],[19675.39, 19675.39, 19675.39],[6030.05, 6030.05, 6030.05],[7.18, 7.18, 7.18],[1, 1, 3],[1, 3, 5],[1, 3, 5],[1, 1, 3],[5, 7, 9],[1, 3, 5],[7, 9, 9],[5, 7, 9],[5, 7, 9]],[[38, 38, 38],[32129.74, 32129.74, 32129.74],[9471.81, 9471.81, 9471.81],[58.93, 58.93, 58.93],[5, 7, 9],[5, 7, 9],[5, 7, 9],[1, 3, 5],[1, 3, 5],[5, 7, 9],[3, 5, 7],[7, 9, 9],[7, 9, 9]],[[44, 44, 44],[59582.77, 59582.77, 59582.77],[18602.53, 18602.53, 18602.53],[517.28, 517.28, 517.28],[3, 5, 7],[3, 5, 7],[3, 5, 7],[3, 5, 7],[3, 5, 7],[5, 7, 9],[5, 7, 9],[5, 7, 9],[5, 7, 9]],[[37, 37, 37],[29288.02, 29288.02, 29288.02],[8489.24, 8489.24, 8489.24],[145.06, 145.06, 145.06],[1, 3, 5],[1, 3, 5],[1, 1, 3],[1, 3, 5],[5, 7, 9],[3, 5, 7],[5, 7, 9],[5, 7, 9],[5, 7, 9]],[[36, 36, 36],[34417.54, 34417.54, 34417.54],[9278.56, 9278.56, 9278.56],[417.5, 417.5, 417.5],[3, 5, 7],[3, 5, 7],[3, 5, 7],[3, 5, 7],[1, 3, 5],[3, 5, 7],[5, 7, 9],[5, 7, 9],[5, 7, 9]],[[41, 41, 41],[3021.99, 3021.99, 3021.99],[656.62, 656.62, 656.62],[6.96, 6.96, 6.96],[1, 1, 3],[1, 3, 5],[1, 3, 5],[1, 1, 3],[5, 7, 9],[3, 5, 7],[5, 7, 9],[5, 7, 9],[5, 7, 9]],[[41, 41, 41],[27270.65, 27270.65, 27270.65],[7819.06, 7819.06, 7819.06],[37.98, 37.98, 37.98],[3, 5, 7],[3, 5, 7],[5, 7, 9],[1, 3, 5],[1, 3, 5],[5, 7, 9],[3, 5, 7],[7, 9, 9],[7, 9, 9]],[[37, 37, 37],[30293.3, 30293.3, 30293.3],[10473.59, 10473.59, 10473.59],[46.68, 46.68, 46.68],[3, 5, 7],[3, 5, 7],[1, 3, 5],[1, 3, 5],[5, 7, 9],[3, 5, 7],[3, 5, 7],[5, 7, 9],[5, 7, 9]],[[37, 37, 37],[22933.38, 22933.38, 22933.38],[7516.61, 7516.61, 7516.61],[23.43, 23.43, 23.43],[1, 3, 5],[1, 3, 5],[1, 1, 3],[1, 3, 5],[5, 7, 9],[3, 5, 7],[5, 7, 9],[5, 7, 9],[5, 7, 9]],[[37, 37, 37],[25541.16, 25541.16, 25541.16],[7371.99, 7371.99, 7371.99],[22.34, 22.34, 22.34],[1, 3, 5],[1, 3, 5],[1, 3, 5],[1, 3, 5],[5, 7, 9],[3, 5, 7],[3, 5, 7],[5, 7, 9],[5, 7, 9]],[[37, 37, 37],[15379.51, 15379.51, 15379.51],[4589.9, 4589.9, 4589.9],[16.57, 16.57, 16.57],[1, 3, 5],[1, 3, 5],[1, 1, 3],[1, 3, 5],[5, 7, 9],[3, 5, 7],[5, 7, 9],[5, 7, 9],[5, 7, 9]],[[42, 42, 42],[29946.62, 29946.62, 29946.62],[9774.62, 9774.62, 9774.62],[32.49, 32.49, 32.49],[3, 5, 7],[1, 3, 5],[1, 3, 5],[1, 3, 5],[5, 7, 9],[1, 3, 5],[5, 7, 9],[5, 7, 9],[5, 7, 9]],[[42, 42, 42],[15348.01, 15348.01, 15348.01],[5529.99, 5529.99, 5529.99],[8.83, 8.83, 8.83],[1, 3, 5],[1, 3, 5],[1, 1, 3],[1, 3, 5],[5, 7, 9],[3, 5, 7],[5, 7, 9],[5, 7, 9],[5, 7, 9]],[[41, 41, 41],[37147.04, 37147.04, 37147.04],[11161.34, 11161.34, 11161.34],[158.17, 158.17, 158.17],[3, 5, 7],[3, 5, 7],[1, 3, 5],[3, 5, 7],[5, 7, 9],[5, 7, 9],[5, 7, 9],[5, 7, 9],[5, 7, 9]],[[42, 42, 42],[19779.39, 19779.39, 19779.39],[6829.25, 6829.25, 6829.25],[11.9, 11.9, 11.9],[1, 3, 5],[1, 3, 5],[1, 3, 5],[1, 3, 5],[5, 7, 9],[3, 5, 7],[5, 7, 9],[5, 7, 9],[5, 7, 9]]])
D4 = np.array([[[42, 42, 42],[27714.01, 27714.01, 27714.01],[8462.43, 8462.43, 8462.43],[16.62, 16.62, 16.62],[1, 1, 3],[1, 1, 3],[1, 1, 3],[1, 1, 3],[7, 9, 9],[3, 5, 7],[3, 5, 7],[1, 3, 5],[3, 5, 7]],[[48, 48, 48],[131675.11, 131675.11, 131675.11],[36371.02, 36371.02, 36371.02],[980.63, 980.63, 980.63],[1, 3, 5],[1, 3, 5],[1, 1, 3],[3, 5, 7],[7, 9, 9],[3, 5, 7],[7, 9, 9],[7, 9, 9],[3, 5, 7]],[[41, 41, 41],[19675.39, 19675.39, 19675.39],[6030.05, 6030.05, 6030.05],[7.18, 7.18, 7.18],[1, 1, 3],[1, 1, 3],[7, 9, 9],[1, 1, 3],[1, 3, 5],[7, 9, 9],[7, 9, 9],[7, 9, 9],[7, 9, 9]],[[38, 38, 38],[32129.74, 32129.74, 32129.74],[9471.81, 9471.81, 9471.81],[58.93, 58.93, 58.93],[7, 9, 9],[1, 3, 5],[7, 9, 9],[1, 3, 5],[1, 3, 5],[7, 9, 9],[7, 9, 9],[3, 5, 7],[7, 9, 9]],[[44, 44, 44],[59582.77, 59582.77, 59582.77],[18602.53, 18602.53, 18602.53],[517.28, 517.28, 517.28],[3, 5, 7],[7, 9, 9],[3, 5, 7],[7, 9, 9],[3, 5, 7],[1, 3, 5],[3, 5, 7],[7, 9, 9],[7, 9, 9]],[[37, 37, 37],[29288.02, 29288.02, 29288.02],[8489.24, 8489.24, 8489.24],[145.06, 145.06, 145.06],[3, 5, 7],[1, 3, 5],[7, 9, 9],[3, 5, 7],[1, 3, 5],[3, 5, 7],[3, 5, 7],[1, 3, 5],[1, 3, 5]],[[36, 36, 36],[34417.54, 34417.54, 34417.54],[9278.56, 9278.56, 9278.56],[417.5, 417.5, 417.5],[7, 9, 9],[1, 3, 5],[7, 9, 9],[7, 9, 9],[1, 3, 5],[1, 3, 5],[3, 5, 7],[1, 3, 5],[1, 3, 5]],[[41, 41, 41],[3021.99, 3021.99, 3021.99],[656.62, 656.62, 656.62],[6.96, 6.96, 6.96],[1, 1, 3],[1, 1, 3],[1, 1, 3],[1, 1, 3],[3, 5, 7],[3, 5, 7],[1, 3, 5],[7, 9, 9],[7, 9, 9]],[[41, 41, 41],[27270.65, 27270.65, 27270.65],[7819.06, 7819.06, 7819.06],[37.98, 37.98, 37.98],[1, 3, 5],[1, 3, 5],[7, 9, 9],[1, 1, 3],[1, 1, 3],[3, 5, 7],[3, 5, 7],[7, 9, 9],[3, 5, 7]],[[37, 37, 37],[30293.3, 30293.3, 30293.3],[10473.59, 10473.59, 10473.59],[46.68, 46.68, 46.68],[7, 9, 9],[1, 3, 5],[7, 9, 9],[3, 5, 7],[1, 1, 3],[7, 9, 9],[7, 9, 9],[1, 3, 5],[7, 9, 9]],[[37, 37, 37],[22933.38, 22933.38, 22933.38],[7516.61, 7516.61, 7516.61],[23.43, 23.43, 23.43],[1, 3, 5],[1, 1, 3],[1, 1, 3],[1, 3, 5],[7, 9, 9],[1, 3, 5],[3, 5, 7],[1, 3, 5],[3, 5, 7]],[[37, 37, 37],[25541.16, 25541.16, 25541.16],[7371.99, 7371.99, 7371.99],[22.34, 22.34, 22.34],[7, 9, 9],[1, 3, 5],[7, 9, 9],[1, 1, 3],[1, 1, 3],[7, 9, 9],[7, 9, 9],[1, 3, 5],[7, 9, 9]],[[37, 37, 37],[15379.51, 15379.51, 15379.51],[4589.9, 4589.9, 4589.9],[16.57, 16.57, 16.57],[1, 3, 5],[1, 3, 5],[1, 3, 5],[1, 3, 5],[7, 9, 9],[1, 3, 5],[1, 3, 5],[1, 3, 5],[3, 5, 7]],[[42, 42, 42],[29946.62, 29946.62, 29946.62],[9774.62, 9774.62, 9774.62],[32.49, 32.49, 32.49],[3, 5, 7],[3, 5, 7],[1, 3, 5],[1, 3, 5],[7, 9, 9],[7, 9, 9],[3, 5, 7],[1, 3, 5],[7, 9, 9]],[[42, 42, 42],[15348.01, 15348.01, 15348.01],[5529.99, 5529.99, 5529.99],[8.83, 8.83, 8.83],[1, 3, 5],[1, 3, 5],[1, 3, 5],[1, 3, 5],[7, 9, 9],[3, 5, 7],[3, 5, 7],[1, 3, 5],[3, 5, 7]],[[41, 41, 41],[37147.04, 37147.04, 37147.04],[11161.34, 11161.34, 11161.34],[158.17, 158.17, 158.17],[7, 9, 9],[1, 3, 5],[7, 9, 9],[3, 5, 7],[3, 5, 7],[3, 5, 7],[7, 9, 9],[7, 9, 9],[3, 5, 7]],[[42, 42, 42],[19779.39, 19779.39, 19779.39],[6829.25, 6829.25, 6829.25],[11.9, 11.9, 11.9],[3, 5, 7],[1, 3, 5],[1, 3, 5],[1, 1, 3],[7, 9, 9],[1, 3, 5],[3, 5, 7],[1, 3, 5],[3, 5, 7]]])

# Pesos de avaliacao de cada especialista.
wk1 = 2
wk2 = 1
wk3 = 1
wk4 = 1

# Calculo da matriz fuzzy de decisao agregada
D = np.ndarray.copy(D1)

for i in range(D.shape[0]):
    for j in range(D.shape[1]):
        D[i][j][0] = min(D1[i][j][0], D2[i][j][0], D3[i][j][0], D4[i][j][0])
        D[i][j][1] = (wk1*D1[i][j][1] + wk2*D2[i][j][1] + wk3*D3[i][j][1] + wk4*D4[i][j][1])/(wk1 + wk2 + wk3 + wk4)
        D[i][j][2] = max(D1[i][j][2], D2[i][j][2], D3[i][j][2], D4[i][j][2])

# Inversao para os criterios de custo
for j in [0, 8]:
    D[:,j] = D[:,j]**(-1)

# Calculo do WPM
WPM_values = []

for i in range(D.shape[0]):
    WPM_values.append(np.array([1.0,1.0,1.0]))
    for j in range(D.shape[1]):
        WPM_values[i] *= np.array([D[i][j][0]**w[j][0],D[i][j][1]**w[j][1],D[i][j][2]**w[j][2]])

print("WPM:")
print(WPM_values)
print("WPM_rank:")
print(sorted(enumerate(WPM_values, start=1), key=lambda x:x[1][2], reverse=True))






