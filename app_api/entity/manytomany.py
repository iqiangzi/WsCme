from sqlalchemy import Table, Column, ForeignKey, String
from .entitybase import Base

TrainingInstitutionAndCategory = \
    Table(
        "TrainingInstitutionAndCategory", Base.metadata,
        Column("TrainingInstitutionId", String(32), ForeignKey("TrainingInstitution.Id"), primary_key=True),
        Column("CategoryId", String(32), ForeignKey("TrainingInstitution_Category.Id"), primary_key=True)
    )

TrainingInstitutionAndType = \
    Table(
        "TrainingInstitutionAndType", Base.metadata,
        Column("TrainingInstitutionId", String(32), ForeignKey("TrainingInstitution.Id"), primary_key=True),
        Column("TypeId", String(32), ForeignKey("TrainingInstitution_Type.Id"), primary_key=True)
    )
