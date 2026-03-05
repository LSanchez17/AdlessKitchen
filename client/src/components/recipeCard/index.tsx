import type { Recipe } from '@/modules/recipes/types';

interface Props {
    recipe: Recipe;
}

const RecipeCard = ({ recipe }: Props) => {
    return (
        <div className="border rounded p-4 mb-4 bg-white">
            <h2 className="text-lg font-semibold mb-2">{recipe.title}</h2>
            <div className="mb-2">
                <strong>Ingredients:</strong>
                <ul className="list-disc list-inside">
                    {recipe.ingredients?.map((ing, idx) => (
                        <li key={idx}>{ing}</li>
                    ))}
                </ul>
            </div>
            <div>
                <strong>Steps:</strong>
                <ol className="list-decimal list-inside">
                    {recipe.steps?.map((step, idx) => (
                        <li key={idx}>{step}</li>
                    ))}
                </ol>
            </div>
        </div>
    );
};

export default RecipeCard;
