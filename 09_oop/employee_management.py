"""Enterprise Workforce Management & Compensation System.

Inspired by Real Python's Object-Oriented Programming (OOP) in Python 3 guide:
https://realpython.com/python3-object-oriented-programming/

This module adapts the core OOP concepts taught in Real Python (class vs instance attributes,
__init__, self, instance methods, dunder methods like __str__ and __repr__, inheritance,
super(), method overriding, and runtime introspection with isinstance/issubclass) into a
professional, enterprise-grade payroll and employee management domain.
"""

from typing import List


class Employee:
    """Base class modeling an enterprise employee in the organization.

    Class Attributes:
        company_name: Global organization name, shared across all instances.
        standard_work_hours: Corporate baseline weekly hours.
        base_annual_leave_days: Default annual PTO entitlement.
        _total_employees: Private class-level counter tracking total headcount.
    """

    # ── CLASS ATTRIBUTES (Shared by all instances of Employee) ──
    company_name: str = "TechCorp Global"
    standard_work_hours: int = 40
    base_annual_leave_days: int = 20
    _total_employees: int = 0

    def __init__(self, emp_id: str, name: str, base_salary: float, department: str) -> None:
        """Initializes a new employee instance.

        Args:
            emp_id: Unique corporate employee identifier (e.g. 'EMP-101').
            name: Full employee name.
            base_salary: Annual base compensation in USD.
            department: Operating department.
        """
        # ── INSTANCE ATTRIBUTES (Unique to each individual object) ──
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary
        self.department = department
        self.remaining_leave_days = Employee.base_annual_leave_days

        # Atomically increment class-level headcount
        Employee._total_employees += 1

    @classmethod
    def get_headcount(cls) -> int:
        """Returns the total number of employees registered across the organization."""
        return cls._total_employees

    def calculate_monthly_pay(self) -> float:
        """Calculates standard gross monthly earnings before taxes."""
        return round(self.base_salary / 12, 2)

    def calculate_annual_bonus(self) -> float:
        """Calculates standard corporate annual bonus (baseline 10% of base salary)."""
        return round(self.base_salary * 0.10, 2)

    def request_leave(self, days: int) -> bool:
        """Requests Paid Time Off (PTO), validating available leave balance.

        Args:
            days: Number of business days requested.

        Returns:
            True if approved, False if rejected due to insufficient days.
        """
        if days <= 0:
            raise ValueError("Leave request must be at least 1 day.")

        if days > self.remaining_leave_days:
            print(
                f"[REJECTED] {self.name} requested {days} days, "
                f"but only {self.remaining_leave_days} days remain."
            )
            return False

        self.remaining_leave_days -= days
        print(
            f"[APPROVED] {self.name}: {days} days granted. "
            f"Remaining PTO balance: {self.remaining_leave_days} days."
        )
        return True

    def __str__(self) -> str:
        """User-friendly representation for reports, invoices, and notification emails."""
        return f"{self.name} ({self.emp_id}) - {self.department} | ${self.base_salary:,.2f}/yr"

    def __repr__(self) -> str:
        """Unambiguous technical representation for logging, tracebacks, and debugging."""
        return (
            f"Employee(emp_id={self.emp_id!r}, name={self.name!r}, "
            f"base_salary={self.base_salary}, department={self.department!r})"
        )


class SoftwareEngineer(Employee):
    """Child class specialized for technical engineering roles.

    Demonstrates inheritance, specialized domain attributes, method extension
    via super(), and overriding.
    """

    def __init__(
        self,
        emp_id: str,
        name: str,
        base_salary: float,
        tech_stack: List[str],
        on_call: bool = False,
    ) -> None:
        # Delegate common initialization to parent Employee via super()
        super().__init__(emp_id, name, base_salary, department="Engineering")
        self.tech_stack = tech_stack
        self.on_call = on_call

    def deploy_service(self, service_name: str, environment: str = "production") -> str:
        """Specialized engineering method."""
        return (
            f"[DEPLOY] {self.name} successfully deployed '{service_name}' "
            f"to {environment} using {self.tech_stack}."
        )

    def calculate_annual_bonus(self) -> float:
        """Overrides and extends parent bonus logic using super().

        Engineering compensation combines:
        - Baseline 10% corporate bonus (from parent class)
        - $5,000 on-call rotation stipend (if on-call)
        - $500 per certified technology in tech_stack
        """
        base_bonus = super().calculate_annual_bonus()
        on_call_stipend = 5000.0 if self.on_call else 0.0
        tech_allowance = len(self.tech_stack) * 500.0

        return round(base_bonus + on_call_stipend + tech_allowance, 2)

    def __repr__(self) -> str:
        return (
            f"SoftwareEngineer(emp_id={self.emp_id!r}, name={self.name!r}, "
            f"base_salary={self.base_salary}, tech_stack={self.tech_stack!r}, on_call={self.on_call})"
        )


class SalesExecutive(Employee):
    """Child class specialized for revenue-generating sales positions.

    Demonstrates complete method overriding where the child implements an entirely
    different bonus compensation formula (commission-based).
    """

    def __init__(
        self,
        emp_id: str,
        name: str,
        base_salary: float,
        commission_rate: float,
        annual_sales_volume: float = 0.0,
    ) -> None:
        super().__init__(emp_id, name, base_salary, department="Sales & Revenue")
        self.commission_rate = commission_rate
        self.annual_sales_volume = annual_sales_volume

    def record_sale(self, amount: float) -> None:
        """Records a closed business deal."""
        self.annual_sales_volume += amount
        print(
            f"[DEAL CLOSED] {self.name} closed ${amount:,.2f}. "
            f"Total volume: ${self.annual_sales_volume:,.2f}"
        )

    def calculate_annual_bonus(self) -> float:
        """Overrides parent bonus calculation with pure sales commission."""
        return round(self.annual_sales_volume * self.commission_rate, 2)

    def __repr__(self) -> str:
        return (
            f"SalesExecutive(emp_id={self.emp_id!r}, name={self.name!r}, "
            f"base_salary={self.base_salary}, commission_rate={self.commission_rate}, "
            f"annual_sales_volume={self.annual_sales_volume})"
        )


def run_workforce_demo() -> None:
    """Demonstrates all Real Python OOP concepts in a professional environment."""
    print("=" * 60)
    print("1. CLASS ATTRIBUTES, INSTANCE ATTRIBUTES & INSTANTIATION")
    print("=" * 60)

    emp1 = Employee("EMP-101", "Elena Vance", 85000.0, "Infrastructure")
    emp2 = Employee("EMP-102", "Marcus Holloway", 92000.0, "Security")

    print(f"emp1: {emp1.name} | Company: {emp1.company_name} | Salary: ${emp1.base_salary:,.2f}")
    print(f"emp2: {emp2.name} | Company: {emp2.company_name} | Salary: ${emp2.base_salary:,.2f}")
    print(f"Total Headcount across company: {Employee.get_headcount()}")

    print("\n" + "=" * 60)
    print("2. DUNDER METHODS: __str__ and __repr__")
    print("=" * 60)
    dev = Employee("EMP-200", "Alex Mercer", 98000.0, "Backend")
    print("str(dev)  ->", str(dev))
    print("repr(dev) ->", repr(dev))

    print("\n" + "=" * 60)
    print("3. INHERITANCE, METHOD OVERRIDING & super()")
    print("=" * 60)

    lead_dev = SoftwareEngineer(
        emp_id="SWE-301",
        name="Sarah Connor",
        base_salary=130000.0,
        tech_stack=["Python", "FastAPI", "Kubernetes", "AWS"],
        on_call=True,
    )

    sales_lead = SalesExecutive(
        emp_id="SLS-401",
        name="Jordan Belfort",
        base_salary=60000.0,
        commission_rate=0.08,
        annual_sales_volume=1_250_000.0,
    )

    print("Lead Dev Monthly Pay (Inherited):", f"${lead_dev.calculate_monthly_pay():,.2f}")
    print(lead_dev.deploy_service("payment-gateway", "production"))

    # Overridden bonus with super()
    print(f"Lead Dev Bonus (Base + On-Call + Certs): ${lead_dev.calculate_annual_bonus():,.2f}")
    # Overridden bonus with commission
    print(f"Sales Lead Bonus (8% Commission):        ${sales_lead.calculate_annual_bonus():,.2f}")

    print("\n" + "=" * 60)
    print("4. POLYMORPHISM & RUNTIME INTROSPECTION (isinstance / issubclass)")
    print("=" * 60)

    roster: List[Employee] = [
        Employee("GEN-001", "Robert Taylor", 72000.0, "Human Resources"),
        lead_dev,
        sales_lead,
    ]

    print("=== ANNUAL PAYROLL & BONUS REPORT ===")
    total_bonus = 0.0
    for employee in roster:
        bonus = employee.calculate_annual_bonus()
        total_bonus += bonus
        print(f"• {employee.name:<16} | Dept: {employee.department:<18} | Bonus: ${bonus:>10,.2f}")
    print(f"\nTotal Bonus Pool Allocated: ${total_bonus:,.2f}")

    print("\n=== RUNTIME INTROSPECTION ===")
    print(f"isinstance(lead_dev, Employee):          {isinstance(lead_dev, Employee)}")
    print(f"isinstance(lead_dev, SoftwareEngineer):  {isinstance(lead_dev, SoftwareEngineer)}")
    print(f"isinstance(lead_dev, SalesExecutive):    {isinstance(lead_dev, SalesExecutive)}")
    print(f"issubclass(SoftwareEngineer, Employee):  {issubclass(SoftwareEngineer, Employee)}")
    print(f"issubclass(Employee, SoftwareEngineer):  {issubclass(Employee, SoftwareEngineer)}")


if __name__ == "__main__":
    run_workforce_demo()
