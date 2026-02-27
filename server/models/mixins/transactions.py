from datetime import datetime, timezone

from sqlalchemy import select

class Transactions:
    """
    A mixin that provides common transaction methods for SQLAlchemy models.
    This includes methods for saving, refreshing, updating, discarding, and retrieving records.
    """
    @classmethod
    async def save(_, db):
        try:
            await db.commit()
        except Exception as e:
            await db.rollback()
            raise e

    @classmethod
    async def refresh(_, db, instance):
        await db.refresh(instance)

    @classmethod
    async def update(base_class, db, instance, updates: dict):
        for key, value in updates.items():
            setattr(instance, key, value)
        await base_class.save(db)
        await base_class.refresh(db, instance)

    @classmethod
    async def delete(base_class, db, instance):
        await db.delete(instance)
        await base_class.save(db)

    @classmethod
    async def discard(base_class, db, instance):
        instance.discarded_at = datetime.now(timezone.utc)
        await base_class.save(db)
        await base_class.refresh(db, instance)

    @classmethod
    async def get_by_id(base_class, db, id):
        return await db.get(base_class, id)

    @classmethod
    async def get_by_email(base_class, db, email):
        result = await db.execute(select(base_class).where(base_class.email == email))
        return result.scalar_one_or_none()