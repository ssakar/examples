

**Architecture Overview**  
The system consists of four main components:  
1. **Heptagon Rotation Module**: Manages the spinning polygon, recalculating vertices and edges each frame based on rotation angle.  
2. **Ball Physics Engine**: Updates ball positions under gravity/friction, handles collisions with walls and other balls using vector math.  
3. **Collision Detection System**: Performs edge-based wall collisions and pairwise ball collisions using distance checks and normal vectors.  
4. **Tkinter Rendering Layer**: Draws the heptagon, balls, and numbers using canvas primitives with rotation for spin indication.  

**Technology Stack**  
- **tkinter**: GUI framework for rendering animations and handling the main loop.  
  *Justification*: Required by user for graphics.  
- **numpy**: For vector math in collision response and physics calculations (e.g., velocity reflections).  
  *Justification*: Simplifies vector operations for edge normals and collision physics.  
- **dataclasses**: Encapsulates ball and heptagon properties (e.g., position, velocity, color).  
  *Justification*: Cleanly organizes object data without boilerplate.  
- **math**: Provides trigonometric functions for rotation and angle calculations.  
  *Justification*: Essential for polygon rotation and ball physics.  
- **typing**: Adds type hints for clarity and maintainability.  

**API/Interface Summary**  
- **Ball Class**  
  - `dataclass`: `Ball(x, y, vx, vy, radius, color, number, angular_velocity)`  
  - Methods:  
    - `update(dt)`: Applies gravity/friction to velocity.  
    - `check_wall_collision(edges)`: Returns collision edge if detected.  
    - `collide_ball(other_ball)`: Updates velocities via elastic collision.  
    - `draw(canvas)`: Renders the ball and its rotating number.  

- **Heptagon Class**  
  - `dataclass`: `Heptagon(center_x, center_y, radius, rotation_angle)`  
  - Methods:  
    - `update_rotation(delta_angle)`: Increments rotation angle.  
    - `compute_edges()`: Returns list of edges (start/end points).  
    - `draw(canvas)`: Renders the polygon using current vertices.  

- **Main Functions**  
  - `animate()`: Triggers frame updates (physics/collisions/redraw).  
  - `reflect_velocity(ball, edge_normal)`: Adjusts ball velocity post-wall collision.  

**Key Decisions**  
1. **Collision Detection**:  
   - **Edge-based checks** ensure accurate wall collisions but increase computation.  
   - **Pairwise ball collisions** use O(n\u00b2) checks, manageable with 20 balls.  

2. **Rotation Handling**:  
   - **Fixed frame rate** via `after(16)` (\u224860 FPS) ensures smooth 72\u00b0/sec rotation.  

3. **Spin Indication**:  
   - **Text rotation** implemented via canvas item configuration using ball angular velocity.  

4. **Heptagon Size**:  
   - Radius set to `ball_radius * 20` to ensure containment under gravity.  

5. **Physics Parameters**:  
   - **Gravity**: `0.3 px/frame\u00b2` downward.  
   - **Friction**: Velocity damping factor `0.99` per frame.  
   - **Restitution**: `0.8` (bounce height 80% of drop height).  

Handing off to Senior Software Engineer for implementation.  

