import bpy
import math

try:
    from qiskit import QuantumCircuit
    from qiskit.quantum_info import Statevector, Pauli
except ImportError:
    print("Veuillez installer Qiskit dans Blender")

def vecteur_bloch(qc):
    """Calcule (x, y, z) sur la sphère de Bloch pour 1 qubit."""
    sv = Statevector(qc)
    return (sv.expectation_value(Pauli("X")).real,
            sv.expectation_value(Pauli("Y")).real,
            sv.expectation_value(Pauli("Z")).real)

# --- 1. Trajectoire du Qubit (Respect de l'exercice) ---
trajectoire = []
qc = QuantumCircuit(1)
for _ in range(100):
    qc.ry(0.26, 0)
    qc.rz(0.40, 0)
    trajectoire.append(vecteur_bloch(qc))

# --- 2. Nettoyage et Préparation de la scène ---
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Lumière (Un simple Soleil)
bpy.ops.object.light_add(type='SUN', location=(5, -5, 5))

# Sphère de Bloch (Grille)
bpy.ops.mesh.primitive_uv_sphere_add(radius=2.0)
sphere = bpy.context.active_object
sphere.display_type = 'WIRE'

# Caméra qui regarde la sphère (position dézoomée)
bpy.ops.object.camera_add(location=(8, -8, 6))
cam = bpy.context.active_object
bpy.context.scene.camera = cam
# Ajout d'une contrainte pour que la caméra suive toujours la sphère
contrainte = cam.constraints.new(type='TRACK_TO')
contrainte.target = sphere
contrainte.track_axis = 'TRACK_NEGATIVE_Z'
contrainte.up_axis = 'UP_Y'

# Qubit (Cube)
bpy.ops.mesh.primitive_cube_add(size=0.5)
cube = bpy.context.active_object
mat = bpy.data.materials.new(name="MatQubit")
mat.use_nodes = True
cube.data.materials.append(mat)
bsdf = mat.node_tree.nodes.get('Principled BSDF')

# --- 3. Animation ---
cube.animation_data_clear()

for i, (x, y, z) in enumerate(trajectoire):
    frame = (i * 2) + 1
    
    # Position et Rotation
    cube.location = (x * 2.0, y * 2.0, z * 2.0)
    cube.rotation_euler = (x * math.pi, y * math.pi, z * math.pi)
    
    # Couleur (Normalisée de [-1, 1] vers [0, 1])
    couleur = ((x+1)/2, (y+1)/2, (z+1)/2, 1)
    if bsdf:
        bsdf.inputs['Base Color'].default_value = couleur
        bsdf.inputs['Base Color'].keyframe_insert("default_value", frame=frame)
    
    cube.keyframe_insert("location", frame=frame)
    cube.keyframe_insert("rotation_euler", frame=frame)

bpy.context.scene.frame_end = 200
bpy.context.scene.render.engine = 'BLENDER_EEVEE'
