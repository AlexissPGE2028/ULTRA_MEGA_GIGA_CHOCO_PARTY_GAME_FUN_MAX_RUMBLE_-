extends CharacterBody2D

@export var speed : float = 300.0
@export var jump_velocity : float = -200.0
@export var double_jump_velocity : float = -100.0

@onready var animated_sprite : AnimatedSprite2D = $AnimatedSprite2D
@onready var hud : CanvasLayer = $HUD

var gravity = ProjectSettings.get_setting("physics/2d/default_gravity")
var has_double_jumped : bool = false
var animation_locked : bool = false
var flying : int = 100
var try : int = 0
#var direction : Vector2 = Vector2.ZERO

#func _on_body_entered(body):
	#for child in body.get_children():
		#print("salut")

func _physics_process(delta):
	if not is_on_floor():
		velocity.y += gravity * delta
		flying -= 1
		if flying <= 0:
			flying = 100 + abs(position.y)
			position.y = 100
			position.x = 0
			print("coucou")
			try += 1
			hud.update_score(try)
	else:
		flying = 100 + abs(position.y)/100
		has_double_jumped = false

	if Input.is_action_just_pressed("jump"):
		if is_on_floor():
			velocity.y = jump_velocity
		elif not has_double_jumped:
			velocity.y += double_jump_velocity
			has_double_jumped = true

	var direction = Input.get_axis("left", "right")
	if direction:
		if direction == -1:
			animated_sprite.play("left")
		elif direction == 1:
			animated_sprite.play("right")
		velocity.x = direction * speed
	else:
		animated_sprite.play("idle")
		velocity.x = move_toward(velocity.x, 0, speed)
	move_and_slide()
