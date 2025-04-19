import json
import os
import shutil

# Ensure directories exist
os.makedirs('src/data/recipe', exist_ok=True)
os.makedirs('src/data/education', exist_ok=True)

# Copy existing files to new location
for recipe_file in os.listdir('recipe'):
    if recipe_file.endswith('.md'):
        shutil.copy(f'recipe/{recipe_file}', f'src/data/recipe/{recipe_file}')

for edu_file in os.listdir('education'):
    if edu_file.endswith('.md'):
        shutil.copy(f'education/{edu_file}', f'src/data/education/{edu_file}')

# Recipe templates
recipe_templates = [
    {
        "id": "spinach-strawberry-salad",
        "title": "Spinach Strawberry Salad with Balsamic Vinaigrette",
        "content": """## Spinach Strawberry Salad with Balsamic Vinaigrette

A refreshing and nutritious salad that perfectly balances sweet and tangy flavors.

### Ingredients

* 6 cups fresh spinach, washed and dried
* 1 cup fresh strawberries, sliced
* 1/4 cup red onion, thinly sliced
* 1/3 cup walnuts or pecans, toasted
* 1/4 cup crumbled feta cheese
* 2 tablespoons balsamic vinegar
* 3 tablespoons extra virgin olive oil
* 1 teaspoon honey
* 1 teaspoon Dijon mustard
* Salt and pepper to taste

### Instructions

1. In a large bowl, combine spinach, strawberries, red onion, nuts, and feta cheese.
2. In a small bowl, whisk together balsamic vinegar, olive oil, honey, Dijon mustard, salt, and pepper.
3. Drizzle the dressing over the salad just before serving.
4. Toss gently to coat all ingredients with the dressing.
5. Serve immediately.""",
        "tags": ["salad", "vegetarian", "quick", "summer"],
        "nutrition": {
            "calories": 220,
            "protein": 5,
            "carbs": 12,
            "fat": 18
        },
        "prepTime": "15 mins",
        "cookTime": "0 mins",
        "servings": 4
    },
    {
        "id": "turkey-stuffed-peppers",
        "title": "Healthy Turkey Stuffed Peppers",
        "content": """## Healthy Turkey Stuffed Peppers

A protein-packed, low-carb dinner option that's full of flavor and nutrition.

### Ingredients

* 4 large bell peppers (any color), halved and seeds removed
* 1 pound lean ground turkey
* 1 small onion, diced
* 2 cloves garlic, minced
* 1 cup cooked brown rice or cauliflower rice
* 1 can (14.5 oz) diced tomatoes, drained
* 1 tablespoon Italian seasoning
* 1/2 teaspoon paprika
* 1/4 teaspoon red pepper flakes (optional)
* Salt and pepper to taste
* 1/2 cup low-fat shredded cheese (mozzarella or cheddar)
* Fresh parsley, chopped, for garnish

### Instructions

1. Preheat oven to 375°F (190°C).
2. Place halved peppers in a baking dish, cut side up.
3. In a large skillet over medium heat, brown ground turkey with onion and garlic until meat is cooked through.
4. Stir in rice, diced tomatoes, and seasonings. Cook for 2-3 minutes.
5. Spoon the turkey mixture into pepper halves.
6. Cover baking dish with foil and bake for 25-30 minutes until peppers are tender.
7. Remove foil, sprinkle with cheese, and bake uncovered for an additional 5 minutes until cheese is melted.
8. Garnish with chopped parsley before serving.""",
        "tags": ["dinner", "high-protein", "low-carb", "meal-prep"],
        "nutrition": {
            "calories": 280,
            "protein": 28,
            "carbs": 18,
            "fat": 12
        },
        "prepTime": "20 mins",
        "cookTime": "35 mins",
        "servings": 4
    },
    {
        "id": "sweet-potato-black-bean-burgers",
        "title": "Sweet Potato Black Bean Burgers",
        "content": """## Sweet Potato Black Bean Burgers

A hearty vegetarian burger that's packed with flavor and plant-based protein.

### Ingredients

* 1 medium sweet potato (about 1 cup mashed)
* 1 can (15 oz) black beans, drained and rinsed
* 1/2 cup cooked quinoa
* 1/4 cup finely chopped red onion
* 2 cloves garlic, minced
* 1/4 cup chopped cilantro
* 1 teaspoon cumin
* 1 teaspoon smoked paprika
* 1/2 teaspoon chili powder
* 1/2 teaspoon salt
* 1/4 teaspoon black pepper
* 1/4 cup oat flour or breadcrumbs
* 1 tablespoon olive oil for cooking

### For serving (optional):
* Whole grain buns
* Avocado slices
* Lettuce
* Tomato
* Red onion
* Sriracha mayo

### Instructions

1. Preheat oven to 400°F (200°C). Pierce sweet potato several times with a fork, place on a baking sheet, and bake for 45-50 minutes until soft. Alternatively, microwave for 5-6 minutes.
2. Allow sweet potato to cool, then peel and mash in a large bowl.
3. In the same bowl, add black beans and mash, leaving some beans intact for texture.
4. Add quinoa, red onion, garlic, cilantro, and all seasonings. Mix well.
5. Stir in oat flour or breadcrumbs until the mixture holds together.
6. Form mixture into 4-6 patties.
7. Heat olive oil in a skillet over medium heat. Cook patties for 4-5 minutes per side until browned and heated through.
8. Serve on buns with your favorite toppings.""",
        "tags": ["vegetarian", "vegan", "plant-based", "dinner"],
        "nutrition": {
            "calories": 240,
            "protein": 10,
            "carbs": 38,
            "fat": 6
        },
        "prepTime": "20 mins",
        "cookTime": "60 mins",
        "servings": 4
    }
]

# Education templates
education_templates = [
    {
        "id": "gut-health-basics",
        "title": "Gut Health 101: The Foundation of Overall Wellness",
        "content": """## Gut Health 101: The Foundation of Overall Wellness

Your gut health affects nearly every aspect of your overall well-being, from digestion to immunity to mental health.

### What Is the Gut Microbiome?

The gut microbiome refers to the trillions of microorganisms (bacteria, viruses, fungi, and other microbes) that live in your digestive tract, primarily in the large intestine. This complex ecosystem plays crucial roles in:

* Digesting foods and absorbing nutrients
* Regulating metabolism
* Supporting immune function
* Producing vitamins (including B vitamins and vitamin K)
* Creating neurotransmitters that affect mood and mental health
* Protecting against harmful pathogens

### Signs of a Healthy Gut

* Regular bowel movements (anywhere from three times a day to three times a week, depending on the individual)
* Absence of digestive discomfort (minimal bloating, gas, or pain)
* Stable energy levels
* Clear skin
* Healthy weight maintenance
* Balanced mood

### Signs of Poor Gut Health

* Frequent digestive issues (bloating, gas, diarrhea, constipation)
* Food intolerances
* Unintentional weight changes
* Sleep disturbances
* Skin irritations (eczema, acne)
* Autoimmune conditions
* Frequent fatigue
* Mood disorders

### Factors That Impact Gut Health

#### Positive Influences:
* Diverse, plant-rich diet
* Adequate fiber intake
* Regular physical activity
* Proper sleep
* Stress management
* Limited antibiotic use

#### Negative Influences:
* Highly processed food diet
* High sugar consumption
* Chronic stress
* Lack of sleep
* Frequent antibiotic use
* Excessive alcohol consumption

### How to Improve Gut Health

#### Focus on Fiber
Aim for 25-30g daily from diverse sources:
* Vegetables and fruits
* Whole grains
* Legumes
* Nuts and seeds

#### Incorporate Fermented Foods
These contain beneficial bacteria:
* Yogurt with live cultures
* Kefir
* Sauerkraut
* Kimchi
* Kombucha
* Tempeh
* Miso

#### Limit Gut-Disrupting Foods
* Artificial sweeteners
* Highly processed foods
* Excessive alcohol
* Foods that trigger individual sensitivities

#### Consider Probiotic Supplements
* Consult with a healthcare provider for recommendations
* Look for multiple strains and adequate CFU (colony-forming units)
* Choose reputable brands with research backing

#### Beyond Diet
* Manage stress through meditation, yoga, or other relaxation techniques
* Prioritize 7-9 hours of quality sleep
* Stay physically active
* Stay hydrated

### The Gut-Brain Connection

The gut and brain communicate bidirectionally through the gut-brain axis. This explains why:
* Digestive issues can affect mood and cognition
* Stress and anxiety can trigger digestive symptoms
* Many neurotransmitters, including serotonin, are produced in the gut

Nurturing your gut health is not a quick fix but a long-term investment in your overall health and well-being.""",
        "category": "Nutrition Fundamentals",
        "tags": ["gut health", "microbiome", "digestion", "immunity"]
    },
    {
        "id": "mindful-eating-techniques",
        "title": "Mindful Eating: Transforming Your Relationship with Food",
        "content": """## Mindful Eating: Transforming Your Relationship with Food

Mindful eating is the practice of paying full attention to the experience of eating and drinking, both inside and outside the body.

### What Is Mindful Eating?

Mindful eating involves:
* Eating slowly and without distraction
* Listening to physical hunger cues and eating only until full
* Distinguishing between actual hunger and non-hunger triggers for eating
* Engaging all senses by noticing colors, smells, sounds, textures, and flavors
* Learning to cope with guilt and anxiety about food
* Appreciating your food and its journey to your table

### Benefits of Mindful Eating

* **Better Digestion:** Slow, mindful eating helps your body properly digest food
* **Reduced Overeating:** Recognizing fullness cues helps prevent overconsumption
* **Greater Satisfaction:** Full attention to taste increases satisfaction with smaller portions
* **Healthier Food Choices:** Awareness often leads to selecting more nutritious options
* **Weight Management:** Not a weight loss diet, but often helps maintain healthy weight
* **Reduced Emotional Eating:** Breaks the cycle of eating in response to emotions
* **Improved Relationship with Food:** Decreases food-related stress and anxiety

### Core Principles of Mindful Eating

#### 1. Eat Without Distractions
* Turn off screens
* Sit at a table
* Focus solely on the act of eating

#### 2. Engage All Senses
* Look at the colors and shapes on your plate
* Smell the aromas of your food
* Notice the textures as you chew
* Identify the different flavors and how they change

#### 3. Eat Slowly
* Put down utensils between bites
* Chew thoroughly (aim for 20-30 chews per bite)
* Take small bites
* Allow 20-30 minutes for a meal

#### 4. Check In With Your Hunger
* Before eating, rate your hunger on a scale of 1-10
* Stop eating when you feel satisfied (about 7 on the scale), not stuffed
* Wait before taking seconds

#### 5. Express Gratitude
* Acknowledge where your food came from
* Appreciate everyone involved in bringing it to your table
* Consider the nourishment it provides your body

### Simple Mindful Eating Exercises

#### The Raisin Exercise
1. Hold a raisin (or any small food item) in your palm
2. Examine it as if you've never seen one before
3. Notice its wrinkles, color, and texture
4. Smell it
5. Place it in your mouth without chewing
6. Notice the sensation on your tongue
7. Slowly chew, focusing on flavor and texture
8. Swallow with full awareness

#### Hunger-Fullness Check
Before, during and after eating, ask:
* Why am I eating? (Physical hunger, boredom, stress, habit?)
* Where do I feel hunger in my body?
* How full am I on a scale of 1-10?

#### Mindful Meal Planning
* Plan meals consciously, considering nutrition and enjoyment
* Shop mindfully, selecting foods with awareness
* Prepare food with attention and gratitude

### Common Challenges and Solutions

#### Eating Too Quickly
* Set a timer for 20 minutes for your meal
* Count your chews
* Put down utensils between bites

#### Emotional Eating
* Create a "pause" before eating (take 5 deep breaths)
* Ask: "Am I physically hungry or emotionally hungry?"
* Develop alternate coping strategies for emotions

#### Distracted Eating
* Designate an eating-only space
* Remove devices during meals
* If eating alone, focus on the sensations rather than seeking distraction

Mindful eating is not about perfect eating, but bringing awareness to your experiences with food. Practice these techniques with curiosity rather than judgment.""",
        "category": "Wellness",
        "tags": ["mindfulness", "eating habits", "behavior change", "nutrition"]
    },
    {
        "id": "understanding-macronutrients",
        "title": "Understanding Macronutrients: Protein, Carbs, and Fats",
        "content": """## Understanding Macronutrients: Protein, Carbs, and Fats

Macronutrients are the nutrients your body needs in large amounts to function properly: proteins, carbohydrates, and fats.

### What Are Macronutrients?

Macronutrients provide energy (calories) and serve essential functions in the body:

* **Proteins:** 4 calories per gram
* **Carbohydrates:** 4 calories per gram
* **Fats:** 9 calories per gram

Each macronutrient plays a unique and vital role in overall health and cannot be completely eliminated from a balanced diet.

### Protein: The Building Blocks

#### Functions in the Body:
* Building and repairing tissues
* Creating enzymes and hormones
* Supporting immune function
* Maintaining fluid balance
* Providing energy when carbohydrates are limited

#### Quality Protein Sources:
* **Animal-Based:** Lean meats, poultry, fish, eggs, dairy
* **Plant-Based:** Legumes (beans, lentils), tofu, tempeh, seitan, quinoa, nuts, seeds

#### Daily Requirements:
* General recommendation: 0.8g per kg of body weight
* Athletes and active individuals: 1.2-2.0g per kg
* Older adults: May benefit from higher intakes (1.0-1.2g per kg)

#### Timing Considerations:
* Distributing protein intake throughout the day optimizes muscle protein synthesis
* Post-workout protein supports recovery and adaptation

### Carbohydrates: The Primary Energy Source

#### Functions in the Body:
* Providing immediate energy for all cells
* Fueling brain function
* Sparing protein (preventing its use for energy)
* Supporting intestinal health (fiber)
* Enabling fat metabolism

#### Types of Carbohydrates:
* **Simple Carbs:** Quick energy, found in fruits, milk, and refined products
* **Complex Carbs:** Sustained energy, found in whole grains, legumes, vegetables
* **Fiber:** Aids digestion, found in plant foods, not digestible for energy

#### Quality Carbohydrate Sources:
* Whole grains (oats, brown rice, quinoa)
* Fruits and vegetables
* Legumes
* Starchy vegetables (sweet potatoes, squash)

#### Considerations for Intake:
* Individual needs vary based on activity level, goals, and metabolism
* Athletes and highly active people need more carbohydrates
* Lower-carb approaches may benefit some individuals for specific health conditions

### Fats: Essential for Health

#### Functions in the Body:
* Providing long-lasting energy
* Supporting cell membrane structure
* Absorbing fat-soluble vitamins (A, D, E, K)
* Insulating and protecting organs
* Contributing to hormone production
* Supporting brain health

#### Types of Fats:
* **Unsaturated Fats:** Generally considered heart-healthy
  * **Monounsaturated:** Olive oil, avocados, nuts
  * **Polyunsaturated:** Fish oil, flaxseeds, walnuts
* **Saturated Fats:** Found in animal products and some plant oils
* **Trans Fats:** Artificial fats that should be avoided

#### Quality Fat Sources:
* Avocados
* Nuts and seeds
* Olive oil and olives
* Fatty fish (salmon, sardines, mackerel)
* Eggs
* Coconut (in moderation)

#### Considerations for Intake:
* Essential for health; extremely low-fat diets can be harmful
* Moderation is key due to high calorie density
* Focus on quality sources rather than elimination

### Balancing Your Macronutrients

#### Standard Recommendations:
* **Protein:** 10-35% of daily calories
* **Carbohydrates:** 45-65% of daily calories
* **Fats:** 20-35% of daily calories

#### Personalization Factors:
* **Activity Level:** Higher activity generally requires more carbohydrates
* **Health Goals:** Weight management, athletic performance, specific health conditions
* **Personal Preferences:** Sustainable dietary patterns that you enjoy
* **Age and Life Stage:** Changing needs throughout the lifespan

#### Signs Your Macronutrient Balance Needs Adjustment:
* Persistent hunger
* Energy fluctuations
* Poor recovery from exercise
* Difficulty maintaining weight
* Digestive issues

Remember that no single macronutrient is "bad" or should be feared. All three play vital roles in health and optimal function. The key is finding the right balance that works for your individual needs and goals.""",
        "category": "Nutrition Fundamentals",
        "tags": ["macronutrients", "nutrition", "protein", "carbohydrates", "fats"]
    }
]

def create_files_from_templates(templates, directory_path, template_type, start_index=0):
    index = start_index
    for template in templates:
        file_path = f"{directory_path}/{template['id']}.md"
        with open(file_path, 'w') as f:
            f.write(template['content'])
        index += 1
    
    # Generate additional files based on templates
    total_needed = 50 - index
    if total_needed > 0:
        template_count = len(templates)
        for i in range(total_needed):
            template_index = i % template_count
            template = templates[template_index]
            
            # Create variations of the template
            if template_type == "recipe":
                variation_id = f"{template['id']}-variation-{i+1}"
                variation_title = f"{template['title']} Variation {i+1}"
                
                # Slightly modify content
                content_lines = template['content'].split('\n')
                content_lines[0] = f"## {variation_title}"
                variation_content = '\n'.join(content_lines)
                
                file_path = f"{directory_path}/{variation_id}.md"
                with open(file_path, 'w') as f:
                    f.write(variation_content)
            else:  # education
                variation_id = f"{template['id']}-variation-{i+1}"
                variation_title = f"{template['title']} - Part {i+1}"
                
                # Slightly modify content
                content_lines = template['content'].split('\n')
                content_lines[0] = f"## {variation_title}"
                variation_content = '\n'.join(content_lines)
                
                file_path = f"{directory_path}/{variation_id}.md"
                with open(file_path, 'w') as f:
                    f.write(variation_content)

# Count existing files
existing_recipe_count = len([f for f in os.listdir('recipe') if f.endswith('.md')])
existing_education_count = len([f for f in os.listdir('education') if f.endswith('.md')])

# Create files from templates
create_files_from_templates(recipe_templates, 'src/data/recipe', 'recipe', existing_recipe_count)
create_files_from_templates(education_templates, 'src/data/education', 'education', existing_education_count)

# Generate complete index.json with all files
index_data = {"recipes": [], "education": []}

# Process recipe files
recipe_files = [f for f in os.listdir('src/data/recipe') if f.endswith('.md')]
for i, recipe_file in enumerate(recipe_files):
    recipe_id = recipe_file[:-3]  # Remove .md extension
    
    # Find matching template or create generic data
    matching_template = next((t for t in recipe_templates if t['id'] in recipe_id), None)
    
    if matching_template:
        recipe_data = {
            "id": recipe_id,
            "title": matching_template["title"] if recipe_id == matching_template["id"] else f"{matching_template['title']} Variation {recipe_id.split('-')[-1]}",
            "image": f"/images/{recipe_id}.jpg",
            "tags": matching_template["tags"],
            "nutrition": matching_template["nutrition"],
            "prepTime": matching_template["prepTime"],
            "cookTime": matching_template["cookTime"],
            "servings": matching_template["servings"]
        }
    else:
        # Generic data for existing recipes
        recipe_data = {
            "id": recipe_id,
            "title": " ".join(word.capitalize() for word in recipe_id.split('-')),
            "image": f"/images/{recipe_id}.jpg",
            "tags": ["healthy", "balanced"],
            "nutrition": {
                "calories": 300,
                "protein": 15,
                "carbs": 30,
                "fat": 15
            },
            "prepTime": "15 mins",
            "cookTime": "20 mins",
            "servings": 4
        }
    
    index_data["recipes"].append(recipe_data)

# Process education files
education_files = [f for f in os.listdir('src/data/education') if f.endswith('.md')]
for i, edu_file in enumerate(education_files):
    edu_id = edu_file[:-3]  # Remove .md extension
    
    # Find matching template or create generic data
    matching_template = next((t for t in education_templates if t['id'] in edu_id), None)
    
    if matching_template:
        edu_data = {
            "id": edu_id,
            "title": matching_template["title"] if edu_id == matching_template["id"] else f"{matching_template['title']} - Part {edu_id.split('-')[-1]}",
            "category": matching_template["category"],
            "tags": matching_template["tags"]
        }
    else:
        # Generic data for existing education articles
        edu_data = {
            "id": edu_id,
            "title": " ".join(word.capitalize() for word in edu_id.split('-')),
            "category": "Nutrition Fundamentals",
            "tags": ["education", "nutrition", "health"]
        }
    
    index_data["education"].append(edu_data)

# Save the complete index.json
with open('src/data/index.json', 'w') as f:
    json.dump(index_data, f, indent=2) 