import type { PayloadAction } from '@reduxjs/toolkit';
import { createSlice } from '@reduxjs/toolkit';
import type { User } from './types';
import type { RootState } from '@/store/store';


const initialState: User = {
    token: undefined,
    firstName: undefined,
    lastName: undefined,
    email: undefined,
    id: undefined,
};

const userSlice = createSlice({
    name: 'user',
    initialState,
    reducers: {
        logout(state) {
            state.token = undefined;
            state.firstName = undefined;
            state.lastName = undefined;
            state.email = undefined;
            state.id = undefined;
        },
        setUser(state, action: PayloadAction<User | null>) {
            const user = action.payload;
            state.token = user?.token;
            state.firstName = user?.firstName;
            state.lastName = user?.lastName;
            state.email = user?.email;
            state.id = user?.id;
        },
    },
});

export const { logout, setUser } = userSlice.actions;

export const selectCurrentUser = (state: RootState) => state.users.id;
export const selectIsUserLoggedIn = (state: RootState) => !!state.users.token;

export default userSlice.reducer;
