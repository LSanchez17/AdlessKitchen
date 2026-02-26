from sqlalchemy import select

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

    @staticmethod
    async def get_by_id(cls, db, id):
        return await db.get(cls, id)
    
    @staticmethod
    async def get_by_email(cls, db, email):
        result = await db.execute(select(cls).where(cls.email == email))
        return result.scalar_one_or_none()