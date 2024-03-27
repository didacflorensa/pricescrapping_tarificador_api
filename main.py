from fastapi import FastAPI
from Database.Database import DatabaseSQL
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
sql = DatabaseSQL()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4200",
    "*",
    "http://192.168.77.158",
    "http://192.168.101.70:4200",
    "http://192.168.101.70:4200/"
    "https://2899-193-144-12-35.ngrok-free.app",
    "https://2899-193-144-12-35.ngrok-free.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/posicion/global")
async def get_posicion_global():
    cursor = sql.get_connection().cursor()
    cursor.execute("{call SP_PosicionGlobal()}")
    r = [dict((cursor.description[i][0], value) \
    for i, value in enumerate(row)) for row in cursor.fetchall()]
    return r

@app.get("/pvp/actuales/{idcliente}")
async def get_pvp_actuales(idcliente):
    cursor = sql.get_connection().cursor()
    cursor.execute("{call SP_PVP_Actuales(?)}", (idcliente))
    r = [dict((cursor.description[i][0], value) \
    for i, value in enumerate(row)) for row in cursor.fetchall()]
    return r

@app.get("/pvp/rango")
async def get_pvp_rango():
    cursor = sql.get_connection().cursor()
    cursor.execute("{call SP_RangoPVPR()}")
    r = [dict((cursor.description[i][0], value) \
    for i, value in enumerate(row)) for row in cursor.fetchall()]
    return r


@app.get("/clase/cliente")
async def get_classe_client():
    cursor = sql.get_connection().cursor()
    cursor.execute("{call SP_ClasseClient()}")
    r = [dict((cursor.description[i][0], value) \
    for i, value in enumerate(row)) for row in cursor.fetchall()]
    return r


'''
Tarificador software
'''
@app.get("/tarificador/competencia")
async def get_competencia_flower():
    cursor = sql.get_connection().cursor()
    cursor.execute("{call SP_TR_Flower_Competencias()}")
    r = [dict((cursor.description[i][0], value) \
    for i, value in enumerate(row)) for row in cursor.fetchall()]
    return r

@app.get("/tarificador/competencia/comparativa")
async def get_competencia_flower():
    cursor = sql.get_connection().cursor()
    cursor.execute("{call SP_TR_Comparativa_Competencias()}")
    r = [dict((cursor.description[i][0], value) \
    for i, value in enumerate(row)) for row in cursor.fetchall()]
    return r

@app.get("/tarificador/tarifas/venta/resumen")
async def get_tarifas_venta_resumen():
    cursor = sql.get_connection().cursor()
    cursor.execute("{call SP_TR_Resumen_TarifasVenta()}")
    r = [dict((cursor.description[i][0], value) \
    for i, value in enumerate(row)) for row in cursor.fetchall()]
    return r

@app.get("/tarificador/tarifas/carga")
async def get_tarifas_venta_resumen():
    cursor = sql.get_connection().cursor()
    cursor.execute("{call SP_TR_Tarifas_PrecioCarga()}")
    r = [dict((cursor.description[i][0], value) \
    for i, value in enumerate(row)) for row in cursor.fetchall()]
    return r


@app.get("/tarificador/precios/rango")
async def get_tarifas_venta_resumen():
    cursor = sql.get_connection().cursor()
    cursor.execute("{call SP_TR_RangoPrecio()}")
    r = [dict((cursor.description[i][0], value) \
    for i, value in enumerate(row)) for row in cursor.fetchall()]
    return r


@app.get("/tarificador/precios/rango/pedido")
async def get_tarifas_venta_resumen():
    cursor = sql.get_connection().cursor()
    cursor.execute("{call SP_TR_RangoPrecioTipoPedido()}")
    r = [dict((cursor.description[i][0], value) \
    for i, value in enumerate(row)) for row in cursor.fetchall()]
    return r


