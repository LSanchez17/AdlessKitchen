import type { Response } from "@/api/types";

type MergeOperation = "merge" | "update" | "remove" | "add";

export const mergeState = <T extends { id?: string | number }>(
    state: Record<string, T[]>,
    payload: Response<T>,
    operation: MergeOperation,
    options?: { id?: string | number }
) => {
    const { entity, results } = payload;
    const entityData = state[entity];

    switch (operation) {
        case "merge":
            return mergeData(entityData, results);
        case "update":
            return updateData(entityData, results, options?.id);
        case "remove":
            return removeData(entityData, options?.id);
        case "add":
            return addData(entityData, results);
        default:
            return entityData;
    }
};

const mergeData = <T>(existing: T[] | undefined, incoming: T[]): T[] => {
    if (!existing) return incoming;
    return [...existing, ...incoming];
};

const updateData = <T extends { id?: string | number }>(
    existing: T[] | undefined,
    incoming: Partial<T>[],
    id?: string | number
): T[] => {
    if (!existing) return [];
    if (!id) return existing;
    return existing.map((item) =>
        item?.id === id ? { ...item, ...incoming.find(i => i.id === id) } : item
    );
};

const removeData = <T extends { id?: string | number }>(existing: T[] | undefined, id?: string | number): T[] | null => {
    if (!existing || !id) return existing || null;
    return existing.filter((item) => item?.id !== id);
};

const addData = <T>(existing: T[] | undefined, incoming: T[]): T[] => {
    if (!existing) return incoming;
    return [...existing, ...incoming];
};