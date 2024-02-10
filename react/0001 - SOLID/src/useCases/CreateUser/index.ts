import { CreateUserUseCase } from './CreateUserUseCases';
import { MailTrapMailProvider } from "../../providers/implementations/MailTrapMailProvider";
import { PostgresUserRepository } from "../../repositories/implementations/PostgresUserRepository";
import { CreateUserController } from './CreateUserController';

const postgresUserRepository = new PostgresUserRepository
const mailTrapMailProvider = new MailTrapMailProvider

const createUserUseCase = new CreateUserUseCase(postgresUserRepository,mailTrapMailProvider)

const createUserController = new CreateUserController(createUserUseCase)

export { createUserUseCase, createUserController}