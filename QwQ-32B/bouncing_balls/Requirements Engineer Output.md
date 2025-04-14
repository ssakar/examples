

- ID: REQ-001  
  - Description: The program must display a spinning heptagon rotating at 360 degrees every 5 seconds.  
  - Acceptance Criteria: The heptagon must rotate precisely at 72 degrees per second (360\u00b0/5s). The rotation must be smooth and continuous.  
  - Priority: High  

- ID: REQ-002  
  - Description: 20 balls must be initialized with unique numbers from 1 to 20 and colors from the specified list.  
  - Acceptance Criteria: Each ball has a distinct number and color from the provided palette.  
  - Priority: High  

- ID: REQ-003  
  - Description: All balls must start from the center of the heptagon.  
  - Acceptance Criteria: At program start, all balls are positioned at the heptagon\u2019s center coordinates.  
  - Priority: High  

- ID: REQ-004  
  - Description: Balls must be affected by gravity and friction.  
  - Acceptance Criteria: Balls accelerate downward due to gravity and lose velocity over time due to friction.  
  - Priority: High  

- ID: REQ-005  
  - Description: Balls must bounce off the rotating heptagon walls realistically.  
  - Acceptance Criteria: Collision detection with rotating walls must be accurate. Bounce height must not exceed the heptagon\u2019s radius but must exceed the ball\u2019s radius.  
  - Priority: High  

- ID: REQ-006  
  - Description: Balls must collide with each other with realistic physics.  
  - Acceptance Criteria: Collisions between balls must adjust velocities using elastic collision principles.  
  - Priority: High  

- ID: REQ-007  
  - Description: Ball rotation must be indicated via their numbers.  
  - Acceptance Criteria: The numbers on balls rotate based on angular velocity (e.g., via text orientation).  
  - Priority: Medium  

- ID: REQ-008  
  - Description: The heptagon must be large enough to contain all balls.  
  - Acceptance Criteria: The heptagon\u2019s radius must be sufficiently large to prevent balls from escaping.  
  - Priority: Medium  

- ID: REQ-009  
  - Description: The program must use only the allowed libraries (tkinter, math, numpy, etc.).  
  - Acceptance Criteria: The code does not use Pygame and adheres to the permitted libraries.  
  - Priority: High  

- ID: REQ-010  
  - Description: All code must reside in a single Python file.  
  - Acceptance Criteria: The entire program is contained in one file with no external dependencies.  
  - Priority: High  

Assumptions:  
- Ball spin indication may use text orientation based on angular velocity.  
- The heptagon\u2019s rotation is modeled by updating vertex positions each frame.  
- Friction is applied as linear damping to velocity.  
- Gravity is a constant acceleration (e.g., 0.5 m/s\u00b2).  



- ID: REQ-001  
  - Description: The program must display a spinning heptagon rotating at 360 degrees every 5 seconds.  
  - Acceptance Criteria: The heptagon must rotate precisely at 72 degrees per second (360\u00b0/5s). The rotation must be smooth and continuous.  
  - Priority: High  

- ID: REQ-002  
  - Description: 20 balls must be initialized with unique numbers from 1 to 20 and colors from the specified list.  
  - Acceptance Criteria: Each ball has a distinct number and color from the provided palette.  
  - Priority: High  

- ID: REQ-003  
  - Description: All balls must start from the center of the heptagon.  
  - Acceptance Criteria: At program start, all balls are positioned at the heptagon\u2019s center coordinates.  
  - Priority: High  

- ID: REQ-004  
  - Description: Balls must be affected by gravity and friction.  
  - Acceptance Criteria: Balls accelerate downward due to gravity and lose velocity over time due to friction.  
  - Priority: High  

- ID: REQ-005  
  - Description: Balls must bounce off the rotating heptagon walls realistically.  
  - Acceptance Criteria: Collision detection with rotating walls must be accurate. Bounce height must not exceed the heptagon\u2019s radius but must exceed the ball\u2019s radius.  
  - Priority: High  

- ID: REQ-006  
  - Description: Balls must collide with each other with realistic physics.  
  - Acceptance Criteria: Collisions between balls must adjust velocities using elastic collision principles.  
  - Priority: High  

- ID: REQ-007  
  - Description: Ball rotation must be indicated via their numbers.  
  - Acceptance Criteria: The numbers on balls rotate based on angular velocity (e.g., via text orientation).  
  - Priority: Medium  

- ID: REQ-008  
  - Description: The heptagon must be large enough to contain all balls.  
  - Acceptance Criteria: The heptagon\u2019s radius must be sufficiently large to prevent balls from escaping.  
  - Priority: Medium  

- ID: REQ-009  
  - Description: The program must use only the allowed libraries (tkinter, math, numpy, etc.).  
  - Acceptance Criteria: The code does not use Pygame and adheres to the permitted libraries.  
  - Priority: High  

- ID: REQ-010  
  - Description: All code must reside in a single Python file.  
  - Acceptance Criteria: The entire program is contained in one file with no external dependencies.  
  - Priority: High  

Assumptions:  
- Ball spin indication may use text orientation based on angular velocity.  
- The heptagon\u2019s rotation is modeled by updating vertex positions each frame.  
- Friction is applied as linear damping to velocity.  
- Gravity is a constant acceleration (e.g., 0.5 m/s\u00b2).  

