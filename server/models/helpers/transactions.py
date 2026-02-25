class Transactions:
    @staticmethod
    async def save(_, db):
        try:
            await db.commit()
        except Exception as e:
            await db.rollback()
            raise e

    @staticmethod
    async def refresh(_, db, instance):
        await db.refresh(instance)

    @staticmethod
    async def update(cls, db, instance, updates: dict):
        for key, value in updates.items():
            setattr(instance, key, value)
        await cls.save(db)
        await cls.refresh(db, instance)

    @staticmethod
    async def delete(cls, db, instance):
        await db.delete(instance)
        await cls.save(db)
