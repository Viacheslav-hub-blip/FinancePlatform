import time
from src.finance_api.Services.finance_service import FinanceService


class BuilderCompanySectors:
    def __init__(self, companies: list[str]):
        self.finance_service = FinanceService()
        self.companies: list[str] = companies
        self.sectors_with_companies: dict[str, list[str]] = self._initialize_sectors_with_companies()

    def another_company_in_company_sector(self, company: str) -> list[str]:
        '''Вовзращает другие компании в секторе исходной компании'''

        for sector, companies in self.sectors_with_companies.items():
            if company in companies:
                companies_in_sector: list[str] = self.sectors_with_companies[sector].copy()
                companies_in_sector.remove(company)
                return companies_in_sector


    def _initialize_sectors_with_companies(self) -> dict[str, list[str]]:
        '''
        Создает словарь с секторами и компаниями относящимися к этому сектору
        '''
        sectors_with_companies: dict[str, list[str]] = {}
        for company in self.companies:
            company_sector = self.finance_service.get_company_sector(company)
            if company_sector in sectors_with_companies and company not in sectors_with_companies[company_sector]:
                sectors_with_companies[company_sector].append(company)
            else:
                sectors_with_companies[company_sector] = [company]
        return sectors_with_companies