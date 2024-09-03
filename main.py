import os
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("L'Empereur - Simplified Version")

# Set up game clock
clock = pygame.time.Clock()

# Game state
game_state = {
    "selected_city": None,
    "cities": {
        "Paris": {
            "population": 50000,
            "resources": {"money": 10000, "food": 20000, "supplies": 15000},
            "loyalty": 100,
            "buildings": {"fort": True, "factory": False}
        },
        "Lyon": {
            "population": 30000,
            "resources": {"money": 8000, "food": 15000, "supplies": 10000},
            "loyalty": 90,
            "buildings": {"fort": False, "factory": True}
        }
    },
    "resources": {"money": 50000, "food": 100000, "supplies": 75000},
    "military_units": [
        {"type": "infantry", "strength": 1000, "location": "Paris"},
        {"type": "cavalry", "strength": 500, "location": "Lyon"}
    ]
}

def main_game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle city selection
            city_rects = draw_game_state(window, game_state)
            handle_city_selection(event, city_rects, game_state)

            # Handle city actions if a city is selected
            if game_state["selected_city"]:
                buttons = draw_city_management(window, game_state)
                handle_city_actions(event, game_state, buttons)
        
        # Clear the screen with a black color
        window.fill((0, 0, 0))
        
        # Drawing code
        city_rects = draw_game_state(window, game_state)
        if game_state["selected_city"]:
            draw_city_management(window, game_state)
        
        # Refresh the display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

def draw_game_state(window, game_state):
    font = pygame.font.SysFont(None, 24)
    y_offset = 10
    city_rects = {}
    for city, data in game_state["cities"].items():
        text_surface = font.render(f"{city}: Pop {data['population']} - Money: {data['resources']['money']} - Food: {data['resources']['food']}", True, (255, 255, 255))
        text_rect = text_surface.get_rect(topleft=(10, y_offset))
        window.blit(text_surface, text_rect.topleft)
        city_rects[city] = text_rect
        y_offset += 30

    y_offset += 20
    overall_resources_text = font.render(f"Overall Resources - Money: {game_state['resources']['money']} - Food: {game_state['resources']['food']} - Supplies: {game_state['resources']['supplies']}", True, (255, 255, 255))
    window.blit(overall_resources_text, (10, y_offset))

    return city_rects

def handle_city_selection(event, city_rects, game_state):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        for city, rect in city_rects.items():
            if rect.collidepoint(event.pos):
                print(f"City selected: {city}")
                game_state["selected_city"] = city

def draw_city_management(window, game_state):
    if game_state["selected_city"]:
        font = pygame.font.SysFont(None, 24)
        city_data = game_state["cities"][game_state["selected_city"]]

        y_offset = 100
        text_surface = font.render(f"Managing City: {game_state['selected_city']}", True, (255, 255, 255))
        window.blit(text_surface, (10, y_offset))
        y_offset += 30

        for resource, value in city_data["resources"].items():
            resource_text = font.render(f"{resource.capitalize()}: {value}", True, (255, 255, 255))
            window.blit(resource_text, (10, y_offset))
            y_offset += 30

        building_text = font.render(f"Buildings: Fort - {city_data['buildings']['fort']}, Factory - {city_data['buildings']['factory']}", True, (255, 255, 255))
        window.blit(building_text, (10, y_offset))
        y_offset += 30

        recruit_button = pygame.Rect(10, y_offset, 100, 30)
        pygame.draw.rect(window, (0, 255, 0), recruit_button)
        window.blit(font.render("Recruit", True, (0, 0, 0)), (15, y_offset + 5))

        manage_resources_button = pygame.Rect(120, y_offset, 150, 30)
        pygame.draw.rect(window, (0, 255, 0), manage_resources_button)
        window.blit(font.render("Manage Resources", True, (0, 0, 0)), (125, y_offset + 5))

        return recruit_button, manage_resources_button

def handle_city_actions(event, game_state, buttons):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if game_state["selected_city"]:
            recruit_button, manage_resources_button = buttons

            if recruit_button.collidepoint(event.pos):
                print(f"Recruiting units in {game_state['selected_city']}")
                # Recruitment logic goes here

            elif manage_resources_button.collidepoint(event.pos):
                print(f"Managing resources in {game_state['selected_city']}")
                # Resource management logic goes here

if __name__ == "__main__":
    os.system("cls")
    main_game_loop()
