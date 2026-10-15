import sqlite3

def init_db():

    conn = sqlite3.connect("colegio.db")
    cursor = conn.cursor()

    # 1. Crear las tablas
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS profesores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(100) NOT NULL,
        especialidad VARCHAR(50) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS estudiantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(100) NOT NULL,
        grado VARCHAR(20) NOT NULL,
        correo VARCHAR(100) UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS cursos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        materia VARCHAR(100) NOT NULL,
        profesor_id INTEGER NOT NULL,
        estudiante_id INTEGER NOT NULL,
        FOREIGN KEY (profesor_id) REFERENCES profesores(id),
        FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id)
    );
    """)

    # 2. Limpiar datos previos si ya existían
    cursor.executescript("""
    DELETE FROM cursos;
    DELETE FROM estudiantes;
    DELETE FROM profesores;
    DELETE FROM sqlite_sequence WHERE name IN ('cursos', 'estudiantes', 'profesores');
    """)

    # 3. Insertar 5 Profesores
    cursor.executescript("""
    INSERT INTO profesores (nombre, especialidad) VALUES
    ('Carlos Mendoza', 'Matemáticas'),
    ('Laura Benítez', 'Literatura'),
    ('Roberto Gómez', 'Física'),
    ('Patricia Silva', 'Química'),
    ('Fernando Torres', 'Historia');
    """)

    # 4. Insertar 5 Estudiantes
    cursor.executescript("""
    INSERT INTO estudiantes (nombre, grado, correo) VALUES
    ('Mateo Rossi', '5to Secundaria', 'mateo@estudiante.edu'),
    ('Valentina Paz', '5to Secundaria', 'valentina@estudiante.edu'),
    ('Lucas Mamani', '6to Secundaria', 'lucas@estudiante.edu'),
    ('Camila Flores', '6to Secundaria', 'camila@estudiante.edu'),
    ('Diego Morales', '4to Secundaria', 'diego@estudiante.edu');
    """)

    # 5. Insertar 5 Cursos / Inscripciones
    cursor.executescript("""
    INSERT INTO cursos (materia, profesor_id, estudiante_id) VALUES
    ('Álgebra Superior', 1, 1),
    ('Literatura Universal', 2, 2),
    ('Física Mecánica', 3, 3),
    ('Química Orgánica', 4, 4),
    ('Historia Universal', 5, 5);
    """)

    conn.commit()
    conn.close()
    print("¡Base de datos 'colegio.db' creada e inicializada con éxito!")

def mostrar_datos():
    """Muestra los datos registrados en la base de datos."""
    conn = sqlite3.connect("colegio.db")
    cursor = conn.cursor()

    print("\n=== PROFESORES ===")
    for row in cursor.execute("SELECT * FROM profesores"):
        print(row)

    print("\n=== ESTUDIANTES ===")
    for row in cursor.execute("SELECT * FROM estudiantes"):
        print(row)

    print("\n=== CURSOS ===")
    for row in cursor.execute("SELECT * FROM cursos"):
        print(row)

    conn.close()

if __name__ == "__main__":
    init_db()
    mostrar_datos()