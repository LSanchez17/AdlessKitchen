import type { Response } from "@/api/types";
import type { RecipeExtractionRequest, RecipeExtractionResponse } from "../types/recipe_types";
import api from "@/api/api";

const recipesApi = api.injectEndpoints({
    endpoints: (builder) => ({
        extractRecipeFromUrl: builder.mutation<Response<RecipeExtractionResponse>, RecipeExtractionRequest>({
            query: (body) => ({
                url: "recipes/imports",
                method: "POST",
                body,
            }),
        }),
    }),
});

export const { useExtractRecipeFromUrlMutation } = recipesApi;

export default recipesApi;
