-- datos `estado`
INSERT INTO estado (nombre_estado) VALUES ('activo'), ('deshabilitado');

-- datos `proyectos`
INSERT INTO proyectos (nombre, descripcion, fecha_inicio, fecha_fin) VALUES 
('proyecto solar', 'instalación de paneles solares', '2024-01-10', '2024-06-15'),
('sistema de gestión', 'desarrollo de software ERP', '2024-02-01', '2024-11-30'),
('renovación de red', 'mejora de red de datos', '2023-11-20', '2024-03-10');

-- datos `registroTiempo`
INSERT INTO registroTiempo (nombre, direccion, telefono, correo, fecha_inicio, salario, id_proyectoEmpleado) VALUES 
('carlos lópez', 'av. central 123', '555-0112', 'clopez@etech.cl', '2024-01-10', 300000, 1),
('ana martínez', 'calle luna 45', '555-0234', 'amartinez@etech.cl', '2024-03-20', 250000, 2),
('pedro torres', 'av. sol 789', '555-0345', 'ptorres@etech.cl', '2023-12-01', 280000, 3);

-- datos `empleados`
INSERT INTO empleados (rut, nombre, direccion, telefono, correo, fecha_inicio, salario, fecha_nacimiento, contrasena, id_tipoEmpleado, estado) VALUES 
('12345678-4', 'maría pérez', 'calle ohiggins 123', '555-1234', 'mperez@etech.cl', '2024-01-15', 3200000, '1990-04-10', 'Mperez85!', 1, 1),
('20765432-7', 'juan soto', 'av. real 456', '555-5678', 'jsoto@etech.cl', '2023-09-01', 2800000, '1988-09-22', 'Jsoto456#', 2, 2),
('18654321-6', 'luis herrera', 'calle norte 789', '555-8765', 'lherrera@etech.cl', '2024-05-10', 3000000, '1995-02-14', 'LHerrera789&', 1, 1);

-- datos `informe`
INSERT INTO informe (nombre_informe, fecha_creacion, id_empleado) VALUES 
('reporte mensual', '2024-06-01', 1),
('evaluación semestral', '2024-07-01', 2),
('análisis de cierre', '2024-10-15', 3);

-- datos `departamentos`
INSERT INTO departamentos (departamento_nombre, telefono, id_empleado) VALUES 
('ventas', '555-1111', 1),
('recursos humanos', '555-2222', 2),
('desarrollo', '555-3333', 3);

-- datos `tipoEmpleado`
INSERT INTO tipoEmpleado (tipo, permisos) VALUES 
('administrador', 'acceso_total, editar_empleados'),
('desarrollador', 'acceso_codigo, editar_codigo'),
('analista', 'ver_informes, editar_informes');

-- datos `modulos`
INSERT INTO modulos (id_modulo, nombre) VALUES 
('MOD001', 'gestión de empleados'),
('MOD002', 'desarrollo de proyectos'),
('MOD003', 'análisis y reportes');

-- datos `accesos`
INSERT INTO accesos (id_modulo, id_tipoEmpleado) VALUES 
('MOD001', 1),
('MOD002', 2),
('MOD003', 3);

-- datos `proyectoEmpleado`
INSERT INTO proyectoEmpleado (id_proyecto, id_empleado) VALUES 
(1, 1),
(2, 2),
(3, 3);

-- datos `departamentoEmpleado`
INSERT INTO departamentoEmpleado (id_departamento, id_empleado) VALUES 
(1, 1),
(2, 2),
(3, 3);