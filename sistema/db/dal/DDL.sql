CREATE TABLE tipoEmpleado (
    id_tipoEmpleado INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    tipo VARCHAR(20) NOT NULL,
    permisos VARCHAR(100) NOT NULL
);

CREATE TABLE modulos (
    id_modulo VARCHAR(12) PRIMARY KEY NOT NULL,
    nombre VARCHAR(40) NOT NULL
);

CREATE TABLE estado (
    id_estado INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre_estado VARCHAR(20) NOT NULL
);

CREATE TABLE registroTiempo (
    id_registroTiempo INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,
    direccion VARCHAR(30) NOT NULL,
    telefono VARCHAR(30) NOT NULL,
    correo VARCHAR(30) NOT NULL,
    fecha_inicio DATE NOT NULL,
    salario INTEGER NOT NULL,
    id_proyectoEmpleado INTEGER NOT NULL
);

CREATE TABLE proyectos (
    id_proyecto INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(50) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL
);

CREATE TABLE empleados (
    id_empleado INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    rut VARCHAR(15),
    nombre VARCHAR(30) NOT NULL,
    direccion VARCHAR(30) NOT NULL,
    telefono VARCHAR(30) NOT NULL,
    correo VARCHAR(30) NOT NULL,
    fecha_inicio DATE NOT NULL,
    salario INTEGER NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    contrasena VARCHAR(60) NOT NULL,
    id_tipoEmpleado INTEGER NOT NULL,
    estado INTEGER NOT NULL,
    FOREIGN KEY (estado) REFERENCES estado(id_estado)
);

CREATE TABLE informe (
    id_informe INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre_informe VARCHAR(40) NOT NULL,
    fecha_creacion DATE NOT NULL,
    id_empleado INTEGER NOT NULL,
    FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado)

);

CREATE TABLE proyectoEmpleado (
    id_proyectoEmpleado INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    id_proyecto INTEGER NOT NULL,
    id_empleado INTEGER NOT NULL,
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto),
    FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado)
);

CREATE TABLE departamentos (
    id_departamento INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    departamento_nombre VARCHAR(30) NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    id_empleado INTEGER NOT NULL,
    FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado)
);
CREATE TABLE departamentoEmpleado (
    id_departamentoEmpleado INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    id_departamento INTEGER NOT NULL,
    id_empleado INTEGER NOT NULL,
    FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento),
    FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado)
);


CREATE TABLE accesos (
    id_accesos INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    id_modulo VARCHAR(12) NOT NULL,
    id_tipoEmpleado INTEGER NOT NULL,
    FOREIGN KEY (id_modulo) REFERENCES modulos(id_modulo),
    FOREIGN KEY (id_tipoEmpleado) REFERENCES tipoEmpleado(id_tipoEmpleado)
);