export interface RecipeExtractionRequest {
    url: string;
}

export interface RecipeExtractionResponse {
    taskId: string;
    status: string;
    result: unknown[];
}
