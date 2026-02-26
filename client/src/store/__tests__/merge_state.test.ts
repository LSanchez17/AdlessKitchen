import { mergeState } from "../merge_state";
import type { Response } from "@/api/types";

type Item = { id: number; name: string };

const makeResponse = (entity: string, results: Item[]): Response<Item> => ({
    entity,
    results,
});

describe("mergeState helper", () => {
    let initial: Record<string, Item[]>;

    beforeEach(() => {
        initial = {
            some: [{ id: 1, name: "one" }, { id: 2, name: "two" }],
        };
    });

    test("merge into empty state", () => {
        const payload = makeResponse("other", [{ id: 3, name: "three" }]);
        const result = mergeState(initial, payload, "merge");
        expect(result).toEqual([{ id: 3, name: "three" }]);
    });

    test("merge appends to existing array", () => {
        const payload = makeResponse("some", [{ id: 3, name: "three" }]);
        const result = mergeState(initial, payload, "merge");
        expect(result).toEqual([
            { id: 1, name: "one" },
            { id: 2, name: "two" },
            { id: 3, name: "three" },
        ]);
        // original state stays untouched
        expect(initial.some).toHaveLength(2);
    });

    test("add to undefined key", () => {
        const payload = makeResponse("new", [{ id: 4, name: "four" }]);
        const result = mergeState(initial, payload, "add");
        expect(result).toEqual([{ id: 4, name: "four" }]);
    });

    test("add appends like merge", () => {
        const payload = makeResponse("some", [{ id: 5, name: "five" }]);
        const result = mergeState(initial, payload, "add");
        expect(result).toEqual([
            { id: 1, name: "one" },
            { id: 2, name: "two" },
            { id: 5, name: "five" },
        ]);
    });

    test("remove non-existent id returns same array", () => {
        const payload = makeResponse("some", []);
        const result = mergeState(initial, payload, "remove", { id: 99 });
        expect(result).toEqual(initial.some);
    });

    test("remove existing id filters it out", () => {
        const payload = makeResponse("some", []);
        const result = mergeState(initial, payload, "remove", { id: 1 });
        expect(result).toEqual([{ id: 2, name: "two" }]);
    });

    test("update with matching id modifies item", () => {
        const payload = makeResponse("some", [{ id: 2, name: "TWO" }]);
        const result = mergeState(initial, payload, "update", { id: 2 });
        expect(result).toEqual([
            { id: 1, name: "one" },
            { id: 2, name: "TWO" },
        ]);
    });

    test("update with missing id leaves array unchanged", () => {
        const payload = makeResponse("some", [{ id: 99, name: "nope" }]);
        const result = mergeState(initial, payload, "update", { id: 99 });
        expect(result).toEqual(initial.some);
    });
});
