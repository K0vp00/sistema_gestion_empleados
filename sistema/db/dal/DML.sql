-- Insertar tipos de empleado
INSERT INTO tipoEmpleado (tipo, permisos) VALUES
('Administrador', 'Acceso total'),
('Desarrollador', 'Acceso a desarrollo y informes'),
('Analista', 'Acceso a informes y proyectos');

-- Insertar módulos
INSERT INTO modulos (id_modulo, nombre) VALUES
('MOD01', 'Gestión de Proyectos'),
('MOD02', 'Gestión de Recursos'),
('MOD03', 'Informes');

-- Insertar departamentos
INSERT INTO departamento (departamento_nombre, telefono, id_empleado) VALUES
('Desarrollo', '555-1234', 1),
('Recursos Humanos', '555-5678', 2),
('Administración', '555-8765', 3);

-- Insertar empleados
INSERT INTO empleado (nombre, direccion, telefono, correo, fecha_inicio, salario, fecha_nacimiento, contrasena, id_tipoEmpleado) VALUES
('Juan Pérez', 'Calle Falsa 123', '555-0001', 'juan@example.com', '2024-01-01', 3000, '1990-01-01', 'pass123', 1),
('Ana Gómez', 'Avenida Siempre Viva 456', '555-0002', 'ana@example.com', '2024-02-01', 2500, '1992-05-15', 'pass456', 2),
('Luis Martínez', 'Boulevard Libertad 789', '555-0003', 'luis@example.com', '2024-03-01', 2200, '1988-12-10', 'pass789', 3);

-- Insertar proyectos
INSERT INTO proyecto (nombre, descripcion, fecha_inicio, fecha_fin) VALUES
('Desarrollo de App Móvil', 'Aplicación para gestionar tareas diarias', '2024-01-10', '2024-06-15'),
('Sistema de Gestión de Inventario', 'Sistema para control de stock en tiempo real', '2024-03-05', '2024-09-30');

-- Insertar relación entre empleados y proyectos
INSERT INTO proyectoEmpleado (id_proyecto, id_empleado) VALUES
(1, 1),  -- Juan Pérez asignado al proyecto 1
(1, 2),  -- Ana Gómez asignada al proyecto 1
(2, 3);  -- Luis Martínez asignado al proyecto 2

-- Insertar registros de tiempo
INSERT INTO registroTiempo (nombre, direccion, telefono, correo, fecha_inicio, salario, id_proyectoEmpleado) VALUES
('Juan Pérez', 'Calle Falsa 123', '555-0001', 'juan@example.com', '2024-01-10', 3000, 1),
('Ana Gómez', 'Avenida Siempre Viva 456', '555-0002', 'ana@example.com', '2024-01-10', 2500, 1),
('Luis Martínez', 'Boulevard Libertad 789', '555-0003', 'luis@example.com', '2024-03-05', 2200, 2);

-- Insertar informes
INSERT INTO informe (nombre_informe, fecha_creacion, id_empleado) VALUES
('Informe de Progreso del Proyecto Móvil', '2024-04-01', 1),
('Informe de Inventario', '2024-06-01', 3);

-- Insertar accesos
INSERT INTO accesos (id_modulo, id_tipoEmpleado) VALUES
('MOD01', 1),  -- Administrador tiene acceso a Gestión de Proyectos
('MOD01', 2),  -- Desarrollador tiene acceso a Gestión de Proyectos
('MOD02', 1),  -- Administrador tiene acceso a Gestión de Recursos
('MOD02', 2),  -- Desarrollador tiene acceso a Gestión de Recursos
('MOD03', 1),  -- Administrador tiene acceso a Informes
('MOD03', 2),  -- Desarrollador tiene acceso a Informes
('MOD03', 3);  -- Analista tiene acceso a Informes

-- Insertar datos en la tabla departamentoEmpleado
INSERT INTO departamentoEmpleado (id_departamento, id_empleado) VALUES
(1, 1),  -- Juan Pérez asignado al departamento de Desarrollo
(2, 2),  -- Ana Gómez asignada al departamento de Recursos Humanos
(3, 3);  -- Luis Martínez asignado al departamento de Administración
